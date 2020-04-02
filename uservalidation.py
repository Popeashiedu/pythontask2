import random
import string

user_data = []
while True:
    first_name = input("Please type first name: ")
    print()  # empty print functions called to create space between inputs to make formatting look good
    last_name = input("Please type last name: ")
    print()
    email = input("Please type email: ")
    print()

    user = "User" + " " + first_name  # this identifies unique users by their first names

    pwd = string.ascii_letters
    randletters = "".join(random.choice(pwd) for x in range(random.randint(5, 5)))
    password = first_name[:2] + randletters + last_name[-2:]
    print(f'Your password is {password}. Are you okay with it?')
    print()
    response = input("Type Y for yes and N for no: ")
    print()

    while True:
        if response.lower() == "y":
            print("Your deets are below")
            break

        elif response.lower() == "n":
            print("Please input a password not less than 7 letters long")
            print()
            newpassword = input("....")
            print()
            while len(newpassword) < 7:
                print("password is too short, must be equal to or above 7 characters")
                print()
                break
            else:
                print("Your details:")
                break


    customer = {
        "First name": first_name,
        "Last name": last_name,
        "email": email
    }

    user_details = {user: customer}

    user_data.append(user_details)
    print()
    print(user_data)
    break
