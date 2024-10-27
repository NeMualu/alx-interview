#!/usr/bin/python3
import sys
import signal

# Initialize counters and dictionaries
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """ Print the accumulated statistics. """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """ Handle keyboard interruption and print statistics before exiting. """
    print_stats()
    sys.exit(0)

# Set up signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1

        # Parse the line to extract IP, date, status code, and file size
        parts = line.split()
        if len(parts) >= 7:
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Update total file size
                total_file_size += file_size

                # Update status code counts
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except ValueError:
                pass  # Ignore lines where parsing fails

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise
