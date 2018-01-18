"""
The main idea is to count all the occuring characters(UTF-8) in string. If you have string like this aba then the result should be { 'a': 2, 'b': 1 }

What if the string is empty ? Then the result should be empty object literal { }
"""
from collections import Counter
def count(string):
    # The function code should be here
    if not string:
        return { }
    return Counter(string)


if __name__ == "__main__":
    def test_count():
        assert count(None) == {}
        assert count('aba') == { 'a': 2, 'b': 1 }
