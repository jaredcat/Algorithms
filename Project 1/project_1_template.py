import sys
import time


def bogus_algorithm(s):
    # Do nothing 10 million times, then return 0. This is only here as
    # an example of slow-running code so you can see how timing should
    # work.
    for i in range(10000000):
        pass
    return 0


def main():
    if len(sys.argv) != 3:
        print('error: you must supply exactly two arguments\n\n' +
              'usage: python3 <Python source code file> <text file> <n>')
        sys.exit(1)

    filename = sys.argv[1]
    n = int(sys.argv[2])

    entire_file = open(filename).read()
    print('Loaded "' + filename + '" of length ' + str(len(entire_file)))

    # take only the first n characters of entire_file
    s = entire_file[:n]
    assert(len(s) == n)
    
    start = time.perf_counter()
    x = bogus_algorithm(s)
    end = time.perf_counter()
    print('x = ' + str(x))
    print('elapsed time = ' + str(end - start))

if __name__ == '__main__':
    main()
