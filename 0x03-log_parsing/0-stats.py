#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import sys
import signal

# Function to print the statistics
def print_msg(dict_sc, total_file_size):
    """
    Method to print the accumulated stats
    Args:
        dict_sc: dict of status codes
        total_file_size: total file size so far
    Returns:
        Nothing
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val > 0:
            print("{}: {}".format(key, val))


# Initialize variables
total_file_size = 0
counter = 0
dict_sc = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

# Signal handler for keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_msg(dict_sc, total_file_size)
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parsed_line = line.split()  # split the line into parts

        # Validate the line format (we expect at least 7 parts, with the correct request format)
        if len(parsed_line) > 6 and parsed_line[5] == "\"GET" and parsed_line[6] == "/projects/260":
            counter += 1  # increment the line counter

            # Update the total file size and status code counts
            try:
                total_file_size += int(parsed_line[-1])  # the file size is the last element
                code = parsed_line[-2]  # the status code is the second-to-last element

                if code in dict_sc:
                    dict_sc[code] += 1  # increment the count for the status code

            except (ValueError, IndexError):
                continue  # skip lines with invalid numbers

            # Every 10 lines, print the statistics
            if counter == 10:
                print_msg(dict_sc, total_file_size)
                counter = 0  # reset the counter after printing

finally:
    # Print any remaining stats on normal exit or error
    print_msg(dict_sc, total_file_size)
