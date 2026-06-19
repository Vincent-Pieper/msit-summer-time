def user_wants_updates():
    status_updates = input("Do you wish for updates between inputs? (Y)es / (N)o: ")
    return status_updates.lower().startswith("y")


def user_input_sum(current_sum):
    while True:
        user_input = input("Please type a whole number: ")
        try:
            user_num = int(user_input)
            break
        except ValueError:
            print("Please enter a valid integer.")
    current_sum += user_num
    return current_sum, user_num


def copy_shop(status_updates, user_num, current_sum):
    if status_updates:
        percentage = current_sum / 1000 * 100
        print(
            f"Your input was {user_num}."
            f"You reached {percentage:g} % of the {1000} needed."
        )


def main():
    print("welcome to summer-time!")
    status_updates = user_wants_updates()
    current_sum = 0
    while current_sum < 1000:
        current_sum, user_num = user_input_sum(current_sum)
        copy_shop(status_updates, user_num, current_sum)
    print("Final sum: " + str(current_sum) + ".")
    print("Thank you for using summer-time! It was a blast!")


if __name__ == "__main__":
    main()