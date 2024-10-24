#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import sys
import signal

# Initialize variables
total_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Function to print the statistics
def print_stats():
    global total_size, status_codes_count
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

# Signal handler for keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Register signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
try:
    for line in sys.stdin:
        parts = line.split()

        # Validate format of the input line
        if len(parts) < 7 or parts[5] != "\"GET" or not parts[6].startswith("/projects/260"):
            continue

        # Extract file size and status code
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total size
            total_size += file_size

            # Update status code count
            if status_code in status_codes_count:
                status_codes_count[status_code] += 1

            # Increment the line count
            line_count += 1

            # Print stats after every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except (ValueError, IndexError):
            # Skip lines with invalid file size or status code
            continue

except KeyboardInterrupt:
    # Print stats on keyboard interruption
    print_stats()
    sys.exit(0)

# Print any remaining stats at the end of the input
print_stats()
