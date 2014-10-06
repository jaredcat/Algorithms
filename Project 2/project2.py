import sys
import copy
import time


class DebianPackage(object):
    def __init__(self, name, votes, size):
        self.name = name
        self.votes = votes
        self.size = size

    def name(self):
        return self.name

    def votes(self):
        return self.votes

    def size(self):
        return self.size

    def __str__(self):
        return self.name + " " + self.votes + " " + self.size


def read_packages(file, n):
    with open(file, "r") as f:
        pkg_list = []
        for line in f[1:n]:
            line = line.split(" ")
            new_pkg = DebianPackage(line[0], int(line[1]), int(line[2]))
            pkg_list.append(copy.deepcopy(new_pkg))
    return pkg_list


def subsets(package_list):
    result = [[]]

    return result


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

    print(pkg_list)

    '''start = time.perf_counter()
    f = exhaustive_knapsack(pkg_list, W)
    end = time.perf_counter()
    print('------ n=' + n + ' W=' + W)
    print('    ---Exhaustive search solution ---')
    print(f)
    print('       Elapsed time = ' + str(end - start) + "seconds")'''

if __name__ == '__main__':
    main()