import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

def ask_name_and_greet_user(name) ->str :
    """
    Ask name and greet user.

    The user has to enter his/her name. The function prints the greeting.

    Regular greeting: Hi, [name]. Would you like to have a Hamburger?
    [name] is capitalized, meaning first letter is capital, the rest is lower.

    If the name is Thanos (case insensitive, so thanos and THANOS also count):
    Get out of here, Thanos! Nobody wants to play with you!
    """
    print("What is your {name}?")

    if name.lower() == "thanos":
        print("Get out of here, Thanos! Nobody wants to play with you!")

    else:
        formatted_name = name.capitalize()
        print(f"Hi, {formatted_name}. Would you like to have a Hamburger?")



def calculate_hypotenuse_length(a: float, b: float) -> float:
    """Return hypotenuse value."""
    hypotenuse_value = math.sqrt((a ** 2) + (b ** 2))
    return hypotenuse_value

def calculate_cathetus_length(a: float, c: float) -> float:
    """Return cathetus value."""
    cathetus_value = math.sqrt((c ** 2) - (a ** 2))
    return cathetus_value


def func():
    print("I'm inside the function")


def my_name_is() -> str:
    print("My name is (name)")


def sum_six(num) -> int:
    sum = num + 6
    return sum


def sum_numbers(a, b) -> int:
    return a + b


def usd_to_eur(usd) -> int:
    eur = 0.8 * usd
    return eur






