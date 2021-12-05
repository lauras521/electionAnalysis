# print("Hello World")

# counties1=["Arapahoe","Denver","Jefferson"]
# if counties1[1]=='Denver':
#     print(counties1[1])


# temperature = int(input("What is the temperature outside? " ))

# if temperature > 80:
#     print('Turn on the AC.')
# else:
#     print("Open the windows.")


# ##What is the score?
# score=int(input("What is your test score? "))
# if score>=90:
#     print('Your grade is an A.')
# else:
#     if score>=80:
#         print("Your score is a B.")
#     else:
#         if score>=70:
#             print("Your score is a C.")
#         else:
#             if score>=60:
#                 print("Your score is a D.")
#             else:
#                 print("Your score is an F.")

# scoreelif=int(input("What is your test score? "))
# if scoreelif>=90:
#     print('Your grade is an A.')
# elif scoreelif>=80:
#     print("Your score is a B.")
# elif scoreelif>=70:
#     print("Your score is a C.")
# elif scoreelif>=60:
#     print("Your score is a D.")
# else:
#     print("Your score is an F.")


# counties=["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not in the list of counties.")
# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso is in the list of counties")
# else: 
#     print("Arapahoe and El Paso are not in the list of counties.")
    

# for county in counties:
#     print(county)


# # # Assign a variable for the file to load and the path.
# # file_to_load = 'Resources\election_results.csv'
# # # Open the election results and read the file.
# # election_data = open(file_to_load,"r")

# # #known file path
# # with open(file_to_load) as election_data:
# #    print(election_data)
# #import numpy


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
x=thisdict.items()
print(x)


y = thisdict.values()
print(y)

z=thisdict.keys()
print(z)

for i in thisdict.keys():
    print(i)

for i in thisdict.values():
    print(i)

for x,y in thisdict.items():
    print(x,y)

print(thisdict.get("model"))