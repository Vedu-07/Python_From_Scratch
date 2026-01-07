age = input("Give me a age value: ")
int_age = int(age)

if int_age < 13:
    print("Child")
elif int_age >= 13 and int_age <= 19:
    print("Teenager")
elif int_age >= 20 and int_age <= 59:
    print("Adult")
else:
    print("Senior")
