

# num = [1,2,3]
# num_list = [item + 5 for item in num]
# print(num_list)

# name = "Bipin"

# letter_list = [letter for letter in name]
# print(letter_list)

# range(1,5)

# range_list = [item * 2 for item in range(1,5)]
# print(range_list)

# name = ["Bipin", "Sharma", "Bipin Sharma"]
# name_list = [name for name in name if len(name) <= 5]
# print(name_list)

# names = ["Bipin", "Sharma", "Bipin Sharma"]
# names_list = [name.upper() for name in names if len(name) > 6]
# print(names_list)

# import random

# students = ["Bipin", "Nilesh", "Rahul", "Sneha", "Sona", "Poonam", "Riya", "Shivangi"]

# students_scores = {student: random.randint(1, 100) for student in students}

# students_passed = {key:value for (key,value) in students_scores.items() if value > 35}
# print(students_scores)

# print(students_passed)


# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}



import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)