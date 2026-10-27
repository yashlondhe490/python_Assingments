'''
47. Write a program to check user role (admin, user, guest) using match case.
'''
role = input("Enter your role (admin/user/guest): ").strip().lower()

match role:
    case "admin":
        print("Full access: manage users, edit and delete data")
    case "user":
        print("Limited access: view and edit your own data")
    case "guest":
        print("Read-only access: view public content")
    case _:
        print("Invalid role")