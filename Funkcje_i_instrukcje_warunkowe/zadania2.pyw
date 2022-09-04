def zadania1(numbers, k):
    for number in numbers:
        skip = False
        for second_num in numbers:
            if (number + second_num) == k and number != second_num:
                if number != second_num and not skip:
                    skip = True
                    continue
                return (True, F"{number}", F"{second_num}")
    return False

def zadanie2