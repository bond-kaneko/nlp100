import sys

if __name__ == "__main__":
    target_str = sys.argv[1]

    picked_str = target_str[1] + target_str[3] + target_str[5] + target_str[7]

    print(picked_str)