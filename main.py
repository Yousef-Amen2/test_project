def userWelcomeUser(name):
    return f"Welcome: {name}"


def userInformations():
    user_info = {}

    while True:
        username_input = input("Please Enter Your Name: ").strip()
        if username_input.isdigit() or not username_input:
            print(f"username cannot be empty or a number value.")
            continue
        user_info["username"] = username_input
        break
    while True:
        age_input = input("Please Type Your Age: ").strip()
        if not age_input.isdigit():
            print(f"your age must be a number you give it {age_input}.")
            continue
        user_info["age"] = age_input
        break
    while True:
        gender = input("Enter Your Gender 1-Meal 2-Femeal: ").strip()
        if gender == "meal" or gender == "1":
            gender = "Meal"
        elif gender == "Femeal" or gender == "2":
            gender = "Female"
        else:
            print("Invalid Input.")
            continue

        user_info["gender"] = gender
        break
    userWelcomeUser(user_info["username"])
    for key, value in user_info.items():
        print(f"Your Informations is:{key}: {value}")


userInformations()
