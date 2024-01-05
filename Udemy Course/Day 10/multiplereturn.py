def format_name(f_name, l_name):

    if f_name == "" or l_name == "":
        return "Invalid Input"

    First = f_name.title()
    Last = l_name.title()

    return f"{First} {Last}"

print(format_name(f_name= input("What is your First Name? "), 
                  l_name = input("What is your Last Name? ")))

