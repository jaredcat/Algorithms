import sys
import time


def largest_digit(input_string):
    #empty set
    largest = ""
    for s in input_string:
        if s.isdigit():
            #if new number is larger than current number
            if s > largest:
                largest = s
    #if empty set and is not a 0
    if not largest and largest != 0:
        #there was no numbers found
        return "None"
    else:
        return largest


def longest_string(s):
    longest = ""
    #starts after file header junk and ends if its impossible for a longer string to be found
    for i in range(3, len(s)-4*len(longest)):
        #starts after longest current found string and goes till it would be impossible to find another string
        for j in range(len(longest)+1, len(s)-i-(len(longest)+1)*2):
            find = s[i:i+j]
            #starts after the 'find' and goes till the there's not enough room to fit its equivalent
            for k in range(i+j, len(s)-len(find)-j):
                check = s[k:k+len(find)]
                if check == find:
                    longest = find
                    break
    if longest != "":
        return longest
    return "None"


def main():
    if len(sys.argv) != 3:
        print('error: you must supply exactly two arguments\n\n' +
              'usage: python3 <Python source code file> <text file> <n>')
        sys.exit(1)

    filename = sys.argv[1]
    n = int(sys.argv[2])

    entire_file = open(filename).read()
    print('Loaded "' + filename + '" of length ' + str(len(entire_file)))
    print('n = ' + str(n))

    # take only the first n characters of entire_file
    s = entire_file[:n]
    assert(len(s) == n)

    start = time.perf_counter()
    x = largest_digit(s)
    end = time.perf_counter()
    print('largest digit = ' + str(x))
    print('elapsed time = ' + str(end - start))
    start = time.perf_counter()
    x = longest_string(s)
    end = time.perf_counter()
    print('longest repeated substring = [' + str(x) + ']')
    print('length = ' + str(len(x)))
    print('elapsed time = ' + str(end - start))

if __name__ == '__main__':
    main()
