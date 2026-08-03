day = input("Enter a day of the week: ").lower()
match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("It's a weekday")
    case "saturday" | "sunday":
        print("It's the weekend")
    case _:
        print("That's not a valid day")