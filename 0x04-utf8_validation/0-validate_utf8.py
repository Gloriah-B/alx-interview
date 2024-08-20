#!/usr/bin/python3
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, otherwise False.
    """
    n_bytes = 0

    # Masks for checking the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get the 8 least significant bits of num
        byte = num & 0xFF

        if n_bytes == 0:
            # Determine the number of bytes in  current UTF-8 character
            if (byte & mask1) == 0:
                continue  # 1-byte character
            elif (byte & mask1) and (byte & mask2) == 0:
                return False  # Invalid UTF-8
            else:
                # Determine the number of bytes based on number of leading 1s
                while (byte & mask1):
                    n_bytes += 1
                    byte <<= 1

                # UTF-8 characters can only be 1 to 4 bytes long
                if n_bytes == 1 or n_bytes > 4:
                    return False
        else:
            # Check that the next byte is a continuation byte (i.e., 10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0
