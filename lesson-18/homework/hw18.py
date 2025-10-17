## Homework 2

# import pandas as pd
#
# url = "https://raw.githubusercontent.com/IslomovSH/python-homework/main/lesson-18/homework/task/tackoverflow_qa.csv"
#
# df = pd.read_csv(url)

## Task 1

# df['creationdate'] = pd.to_datetime(df['creationdate'])
# old_questions = df[df['creationdate'] < '2014-01-01']
# old_questions.head()
#
# print(old_questions.head())
# print("\nUmumiy soni:", len(old_questions))

## Task 2

# hsq = df[df['score'] > 50]
# print(hsq.head())
# print("\nUmumiy soni:", len(hsq))

## Task 3

# score_between = df[(df['score'] > 50) & (df['score'] < 100)]
# print(score_between.head())
# print("\nUmumiy soni:", len(score_between))

## Task 4

# scott_questions = df[df['ans_name'] == 'Scott Boston']
# print(scott_questions.head())
# print("\nUmumiy soni:", len(scott_questions))

## Task 5

# users = ['Scott Boston', 'Mike Pennington', 'Demitri', 'doug', 'DarkAnt']
#
# answered_by_users = df[df['ans_name'].isin(users)]
#
# print(answered_by_users.head())
# print("\nUmumiy soni:", len(answered_by_users))

## Task 6

# df['creationdate'] = pd.to_datetime(df['creationdate'])
#
# filtered = df[
#     (df['creationdate'] >= '2014-03-01') &
#     (df['creationdate'] <= '2014-10-31') &
#     (df['ans_name'] == 'Unutbu') &
#     (df['score'] < 5)
# ]
#
# print(filtered.head())
# print("\nUmumiy soni:", len(filtered))

## Task 7

# filtered = df[
#     ((df['score'] > 5) & (df['score'] < 10)) |
#     (df['viewcount'] > 10000)
# ]
#
# print(filtered.head())
# print("\nUmumiy soni:", len(filtered))

## Task 8

# not_scott = df[df['ans_name'] != 'Scott Boston']
# print(not_scott.head())
# print("\nUmumiy soni:", len(not_scott))

## Homework 3

# import pandas as pd
# 
# url = "https://raw.githubusercontent.com/IslomovSH/python-homework/main/lesson-18/homework/task/titanic.csv"
# 
# df = pd.read_csv(url)

## Task 1

# female_class1_20_30 = df[
#     (df['Sex'] == 'female') &
#     (df['Pclass'] == 1) &
#     (df['Age'] >= 20) &
#     (df['Age'] <= 30)
# ]
#
# print(female_class1_20_30)

## Task 2

# high_fare_passengers = df[df['Fare'] > 100]
#
# print(high_fare_passengers)

## Task 3

# alone_survivors = df[
#     (df['Survived'] == 1) &
#     (df['SibSp'] == 0) &
#     (df['Parch'] == 0)
# ]
#
# print(alone_survivors)

## Task 4

# embarked_c_high_fare = df[
#     (df['Embarked'] == 'C') &
#     (df['Fare'] > 50)
# ]
#
# print(embarked_c_high_fare)

## Task 5

# family_passengers = df[
#     (df['SibSp'] > 0) &
#     (df['Parch'] > 0)
# ]
#
# print(family_passengers)

## Task 6

# young_not_survived = df[
#     (df['Age'] <= 15) &
#     (df['Survived'] == 0)
# ]
#
# print(young_not_survived)

## Task 7

# luxury_passengers = df[
#     (df['Cabin'].notnull()) &
#     (df['Fare'] > 200)
# ]
#
# print(luxury_passengers)

## Task 8

# odd_passengers = df[df['PassengerId'] % 2 != 0]
#
# print(odd_passengers)

## Task 9

# unique_ticket_passengers = df[
#     df['Ticket'].duplicated(keep=False) == False
# ]
#
# print(unique_ticket_passengers)

## Task 10

# miss_class1 = df[
#     (df['Name'].str.contains("Miss")) &
#     (df['Pclass'] == 1) &
#     (df['Sex'] == 'female')
# ]
# 
# print(miss_class1)

