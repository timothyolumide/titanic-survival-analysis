# Titanic Survival Analysis

Python (pandas + matplotlib) analysis of who survived the Titanic.

## Question
Which passengers were most likely to survive?

## What I did
•⁠  ⁠Loaded the Kaggle Titanic dataset (891 passengers)
•⁠  ⁠Cleaned the data: 177 missing ages were filled with the median age (28)
•⁠  ⁠Grouped passengers by sex, ticket class and age group
•⁠  ⁠Made three charts

## Findings
•⁠  ⁠Women: 74% survived. Men: 19%.
•⁠  ⁠1st class: 63%. 2nd class: 47%. 3rd class: 24%.
•⁠  ⁠Children (0-12): 58%. Seniors (60+): 23%.

Note: the Cabin column had 687 missing values, so I did not use it.

## Run it
1.⁠ ⁠Download train.csv from the Kaggle Titanic competition and put it in the same folder.
2.⁠ ⁠Install: pip install pandas matplotlib
3.⁠ ⁠Run: python titanic_analysis.py

By Timothy Olumide
