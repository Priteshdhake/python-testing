print("My name is pritesh\n")

print(f"india won by {100} runs\n")

print("*******************************************************")

calculation_to_units = 24
name_of_unit = "hours"

def calculate_num(num):
     print(f"this is the calculation : {num * calculation_to_units} { name_of_unit}\n")

calculate_num(40)

name = "pritesh"

def full_name(nickname,num):
     last_name = "Dhake"
     return(f"{name} {last_name} {nickname} {num}")


show_the_name = input("Enter the nickanme !\n")
the_name = input("Enter the num !\n")
new_name= full_name(show_the_name, the_name)
print(new_name)
      