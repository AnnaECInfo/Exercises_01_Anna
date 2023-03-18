def name_age():
    name = input(f"Please enter your name:")
    print(f"Hello {name}.")
    age = int(input(f"Please enter your age:"))
    print(f"Hello {name}. Your age is: {age}")
    return f"{name}{age}"


def swap_integers(num1,num2):
    print(f"num1 is {num1} and num2 is {num2}")
    temp = num1
    num1 = num2
    num2 = temp
    print(f"now num1 is {num1} and num2 is {num2}")
    return f"{num1}{num2}"

def check_numbers(num1, num2):
    if (num1 % 6 == 0 or num2 % 6 == 0) and (num1 % 10 == 0 and num2 % 10 == 0):
        return (True)
    else:
        return (False)

def sum_up(num1, num2):
    if num1 < num2:
        result = int(sum(range(num1,num2+1)))
        return (result)
    if num1 > num2:
        return f"zero"
    if num1 < 0 and num2 < 0:
        return f"zero"

def circle_area(r1, r2, r3):
    a1 = 3.14 * pow(r1, 2)
    a2 = 3.14 * pow(r2, 2)
    a3 = 3.14 * pow(r3, 2)
    numbers = [a1, a2, a3]
    result_area = float(sum(numbers))
    return (result_area)

def check_string(text):
    if text.endswith("a", "A") or text.startswith("a", "A"):
        return True
    else:
        return False

def triangle(rows):
    for x in range(rows):
        for y in range(x+1):
            print("* ", end="")
        print()
