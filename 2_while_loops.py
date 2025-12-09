# Given:
colors = ["red", "blue", "green", "yellow", "purple"]

# Challenge:
# Use a while loop to print each color UNTIL you find "yellow".
# Do NOT print "yellow" — stop before it.


# for x in colors:
#     if x == "yellow":
#         break
#     else:
#         print(x)

index = 0
while index < len(colors):
    if colors [index] == "yellow":
        break
    print(colors[index])
    index += 1






# name = input("What is your name? ")

# while name == "":
#     print("You did not enter your name")
    

#     print(f"Hello {name}")

# age = int(input("Enter your age "))

# while age <0 :
#     print("Age can't be negative!")
#     age = int(input("Enter your age"))

# print(f"You are {age} years old")

# food = input("Enter a food you like (q to quit): ")

# food_list = []


# while not food == "q":
#     print(f"You like {food}")
#     food_list.append(food)
#     food = input("Enter a food you like (q to quit): ")

# print("bye")


# print(food_list)


# num = int(input("Enter a number between 1 and 10 : "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a number between 1 and 10 : "))


# print(f"Your number is {num}")


