# print("welcome to the rollercoaster! ")
# height = int(input("What is your height in cm?\n"))
#
# if height >= 120:
#     print("You can ride")
#     age = int(input("Enter your age : "))
#     if age <= 12:
#         print("Please pay = $5")
#     elif age <= 18:
#         print("Please pay = $7")
#     else:
#         print("Please pay $12")
#
# else:
#     print("you can not")



#  ----------- bmi ------

# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
# # 🚨 Do not modify the values above
# # Write your code below 👇
#
# if bmi < 18.5:
#     print("underweight")
# elif bmi < 25:
#     print("normal weight")
# else:
#     print("overweight")


#    ------ Rollercoaster more update problem -------

print("welcome to the rollercoaster! ")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("You can ride")
    age = int(input("Enter your age : "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5 ")
    elif age <= 18:
        bill = 7
        print("Youths ticket are $7 ")
    else:
        bill = 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want to have a photo take ? Type Y for Yes and N for No.\n")
    if wants_photo.upper() == "Y":
        bill += 3

    print(f"your final bill is ${bill}")

else:
    print("you can not")

