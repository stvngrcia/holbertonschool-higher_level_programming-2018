#!/usr/bin/python3
import sys


def print_status():
    '''
        Printing the status of the request
    '''
    counter = 0
    file_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    for l in sys.stdin:
        try:
            counter += 1
            for code, val in status_codes.items():
                if (code in l):
                    status_codes[code] = val + 1
            my_list = l.split()
            file_size += int(my_list[-1])
            if counter == 10:
                print("File size: {:d}".format(file_size))
                for code, val in sorted(status_codes.items()):
                    if (val != 0):
                        print("{}: {}".format(code, val))
                        counter = 0
        except KeyboardInterrupt:
            print("File size: {:d}".format(file_size))
            for code, val in status_codes.items():
                    if (val != 0):
                        print("{}: {}".format(code, val))
    if counter < 9:
            print("File size: {:d}".format(file_size))
            for code, val in status_codes.items():
                    if (val != 0):
                        print("{}: {}".format(code, val))


if __name__ == "__main__":
    print_status()
