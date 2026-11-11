def ask_question(name):
    answer = input(f"How was your day, {name}? ")

    if answer == "Good":
        print(f"That's great, {name}")
    elif answer == "Bad":
        print(f"Sorry to hear that, {name}")
    else:
        print(f"What, {name}?")






def main():
    name = input("Enter your name:")
    print (f"Hello, {name}")
    ask_question(name)
if __name__ == "__main__":
    main()


