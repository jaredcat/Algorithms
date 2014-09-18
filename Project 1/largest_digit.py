import sys
import time





def main():
    input_string = input("Type a string containing numbers: ")
    start = time.perf_counter()
    x = largest_digit(input_string)
    end = time.perf_counter()
    print('x = ' + str(x))
    print('elapsed time = ' + str(end - start))

if __name__ == '__main__':
    main()
