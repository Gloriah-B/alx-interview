#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Method that determines if a given data set
    represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, otherwise False.
    """
    nbytes = 0

    b1 = 1 << 7  # 10000000
    b2 = 1 << 6  # 01000000

    for i in data:
        if nbytes == 0:
            # Determine how many bytes are in the current UTF-8 character
            b = 1 << 7
            while b & i:
                nbytes += 1
                b >>= 1

            # UTF-8 characters can be 1 to 4 bytes long
            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            # Check that current byte is a valid continuation byte (10xxxxxx)
            if not (i & b1 and not (i & b2)):
                return False

        nbytes -= 1

    return nbytes == 0
