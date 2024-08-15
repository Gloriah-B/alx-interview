#!/usr/bin/python3
import sys
import signal


def print_stats(total_size, status_codes):
    """Prints the accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """Parses a log line and extracts the relevant information if it matches the format."""
    try:
        parts = line.split()
        if len(parts) < 7:
            return None, None

        file_size = int(parts[-1])
        status_code = parts[-2]

        if status_code in ['200', '301', '400', '401', '403', '404', '405', '500']:
            return file_size, status_code
        else:
            return None, None
    except (IndexError, ValueError):
        return None, None


def main():
    total_size = 0
    status_codes = {code: 0 for code in ['200', '301', '400', '401', '403', '404', '405', '500']}
    line_count = 0

    def signal_handler(sig, frame):
        """Handles the keyboard interruption signal (CTRL + C) and prints stats."""
        print_stats(total_size, status_codes)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            file_size, status_code = parse_line(line)
            if file_size is not None and status_code is not None:
                total_size += file_size
                status_codes[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
