from profile import show_profile

while True:
    print("=== メニュー ===")
    print("1: プロフィール入力")
    print("2: 終了")

    choice = input("選択してください: ")

    if choice == "1":
        show_profile()
    elif choice == "2":
        print("終了します")
        break
    else:
        print("もう一度選んでください")
