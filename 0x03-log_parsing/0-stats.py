#!/usr/bin/python3
import sys

def print_stats(status_codes, total_file_size):
    """
    Prints the accumulated metrics.
    Args:
        status_codes (dict): Dictionary of status codes.
        total_file_size (int): Total size of all files.
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(status_codes.items()):
        if val > 0:
            print("{}: {}".format(key, val))

def main():
    total_file_size = 0
    counter = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

    try:
        for line in sys.stdin:
            parsed_line = line.split()[::-1]  # Trim and reverse the line parts

            if len(parsed_line) > 2:
                counter += 1
                total_file_size += int(parsed_line[0])  # Extract file size
                code = parsed_line[1]  # Extract status code

                if code in status_codes:
                    status_codes[code] += 1

                if counter == 10:
                    print_stats(status_codes, total_file_size)
                    counter = 0

    except Exception:
        pass
    finally:
        print_stats(status_codes, total_file_size)

if __name__ == "__main__":
    main()

