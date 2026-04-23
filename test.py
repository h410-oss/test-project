from profile import show_profile

while True:
    print("=== MENU ===")
    print("1: Profile")
    print("2: Exit")
    
    choice = input("Select: ")

    if choice == "1":
        show_profile()
    elif choice == "2":
        print("exit")
        break
    else:
        print("reselect")
