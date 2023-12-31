import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""

    assert repeat_string("Python", 1) == "Python"

    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    test_car = Car()
    assert test_car.fuel == 0


def phrase_to_sentence(phrase):
    # capitalise the first letter
    sentence = phrase.capitalize()
    # add the full stop, but only if we need to
    if sentence[-1] != '.':
        sentence += '.'
    return sentence


run_tests()

doctest.testmod()
