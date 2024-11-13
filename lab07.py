#V00701600 Daliyah Holliday

# Constants
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"

# Functions
def is_alpha(s):
    """Returns True if all characters in the string are ASCII letters."""
    for char in s:
        if char not in ASCII_LOWERCASE and char not in ASCII_UPPERCASE:
            return False
    return True

def is_digit(s):
    """Returns True if all characters in the string are ASCII decimal digits."""
    for char in s:
        if char not in DECIMAL_DIGITS:
            return False
    return True


