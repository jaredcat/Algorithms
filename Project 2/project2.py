import sys
import time


class DebianPackage(object):
    def __init__ (self, name, votes, size):
        self.name = name
        self.votes = votes
        self.size = size

    def return_values(self):
        return self.name, self.votes, self.size


def read_packages(file, n):
    f = open(file, "r")
    pkg = DebianPackage()
    pkg_list = []
    first = 1
    for line in f:
        if not first:
            line = line.split(" ")
            pkg.initialize(line[0], int(line[1]), int(line[2]))
            pkg_list.append(pkg)
        else:
            first = 0
    f.close()
    return pkg_list


def subsets(package_list):
    return 0


def verify_knapsack(candiate, W):
    return 0


def compare_knapsack(candidate, best):
    return 0


def exhaustive_knapsack(package_list, W):
    best = None
    for candidate in subsets(package_list):
        if verify_knapsack(candiate, W):
            if compare_knapsack(candidate, best):
                best = candidate
    return best


def main():
    '''if len(sys.argv) != 4:
        print('error: you must supply exactly two arguments\n\n' +
              'usage: python3 <Python source code file> <text file> <n> <W>')
        sys.exit(1)

    filename = sys.argv[1]
    n = int(sys.argv[2])+1
    W = int(sys.argv[3])'''
    filename = "packages.txt"
    n = 23
    W = 2000

    pkg_list = read_packages(filename, n)

    start = time.perf_counter()
    f = exhaustive_knapsack(pkg_list, W)
    end = time.perf_counter()
    print('------ n=' + n + ' W=' + W)
    print('    ---Exhaustive search solution ---')
    print(f)
    print('       Elapsed time = ' + str(end - start) + "seconds")

if __name__ == '__main__':
    main()