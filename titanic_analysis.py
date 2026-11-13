import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

# Clean: fill the 177 missing ages with the median age
df["Age"] = df["Age"].fillna(df["Age"].median())


def bar_chart(labels, values, colors, title, filename, size=(7, 5)):
    plt.figure(figsize=size)
    bars = plt.bar(labels, values, color=colors)
    plt.title(title, fontsize=16, fontweight="bold")
    plt.ylabel("Survival rate (%)")
    plt.ylim(0, 100)
    for bar in bars:
        h = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, h + 2, f"{h:.0f}%", ha="center", fontsize=13, fontweight="bold")
    plt.savefig(filename, dpi=200, bbox_inches="tight")
    plt.close()


# Chart 1: survival by sex
sex = df.groupby("Sex")["Survived"].mean() * 100
bar_chart(["Female", "Male"], [sex["female"], sex["male"]], ["#2F6BEA", "#0B1E5B"],
          "Titanic: Who Survived?", "survival_by_sex.png")

# Chart 2: survival by ticket class
cls = df.groupby("Pclass")["Survived"].mean() * 100
bar_chart(["1st class", "2nd class", "3rd class"], [cls[1], cls[2], cls[3]],
          ["#4F86F7", "#2F6BEA", "#0B1E5B"],
          "Titanic: Survival by Ticket Class", "survival_by_class.png")

# Chart 3: survival by age group
labels = ["Child 0-12", "Teen 13-18", "Adult 19-35", "Adult 36-60", "Senior 60+"]
df["AgeGroup"] = pd.cut(df["Age"], bins=[0, 12, 18, 35, 60, 100], labels=labels)
age = df.groupby("AgeGroup", observed=True)["Survived"].mean() * 100
bar_chart(labels, [age[l] for l in labels],
          ["#8DB4FF", "#4F86F7", "#2F6BEA", "#1B3FA0", "#0B1E5B"],
          "Titanic: Survival by Age Group", "survival_by_age.png", size=(9, 5))

print("Done: 3 charts saved")