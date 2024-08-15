#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys

# Initialize counters and tracking variables
i = 0
sum_file_size = 0
status_code = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}

def print_stats():
    """Prints the accumulated metrics."""
    print('File size: {:d}'.format(sum_file_size))
    for key in sorted(status_code.keys()):
        if status_code[key] > 0:
            print('{}: {}'.format(key, status_code[key]))

try:
    for line in sys.stdin:
        args = line.split()
        if len(args) > 2:
            status_line = args[-2]
            file_size = args[-1]

            # Update metrics if the status code is valid
            if status_line in status_code:
                status_code[status_line] += 1
            sum_file_size += int(file_size)
            i += 1

            # Print stats after every 10 lines
            if i == 10:
                print_stats()
                i = 0
except Exception:
    pass
finally:
    print_stats()
