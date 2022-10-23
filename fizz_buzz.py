def fizz_buzz(number: int):
    """

    :param number:
    :return:
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


input("Play fizz buzz.  Press enter to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_amswer = fizz_buzz(next_number)
    player_answer = input("You go: ")
    if player_answer != correct_amswer:
        print("You lose,the correct answer was {}:".format(correct_amswer))
        break
    else:
        print("Well done you have reached {}:".format(next_number))
