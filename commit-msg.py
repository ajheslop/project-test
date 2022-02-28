#!/usr/bin/python3

import sys


class bcolors:
    OKCYAN = '\033[96m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def main():
    messageFile = sys.argv[1]
    try:
        file = open(messageFile, 'r')
        message = file.read()
    finally:
        file.close()
    is_valid = len(message.split(" ")) > 5
    if not is_valid:
        print(f"{bcolors.WARNING}WARNING: Commit message less than 5 words.{bcolors.ENDC}")
        print(f"{bcolors.OKCYAN}Try commiting again with verbose commit message{bcolors.ENDC}\n")
        print(f"{bcolors.FAIL}Error: Commit Failed.{bcolors.ENDC}")
    sys.exit(0 if is_valid else 1)

if __name__ == "__main__":
    main()