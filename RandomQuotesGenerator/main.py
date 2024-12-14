from quotes import get_random_quote

if __name__ == "__main__":
    print("Welcome to the Random Quotes Generator!")
    while True:
        print("\nHere's your random quote:")
        print(get_random_quote())
        choice = input("\nDo you want another quote? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Goodbye!")
            break
