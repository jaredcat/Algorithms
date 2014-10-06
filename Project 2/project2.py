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
        return self.name + " " + str(self.size) + " " + str(self.votes)


def read_packages(file, n):
    first = 1
    i = 0
    with open(file, "r") as f:
            pkg_list = []
            for line in f:
                if not first:
                    if i == n:
                        break
                    line = line.split(" ")
                    new_pkg = DebianPackage(line[0], int(line[1]), int(line[2]))
                    pkg_list.append(copy.deepcopy(new_pkg))
                    i += 1
                else:
                    first = 0
                    i += 1
    return pkg_list


def subsets(package_list):
    result = [[]]
    for x in package_list:
        with_x = []
        for subset in result:
            with_x.append(subset + [x])
        result = result + with_x
    return result


def verify_knapsack(candiate, W):
    sum = 0
    for x in candiate:
        sum += x.size
    if sum > W:
        return 0
    else:
        return 1


def compare_knapsack(candidate, best):
    candidate_votes = 0
    best_votes = 0
    for x in candidate:
        candidate_votes += x.votes
    for x in best:
        best_votes += x.votes
    if candidate_votes <= best_votes:
        return 0
    else:
        return 1


def exhaustive_knapsack(package_list, W):
    best = []
    for candidate in subsets(package_list):
        if verify_knapsack(candidate, W):
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
    n = 20+1
    W = 1000

    pkg_list = read_packages(filename, n)

    start = time.perf_counter()
    f = exhaustive_knapsack(pkg_list, W)
    end = time.perf_counter()
    print('------ n=' + str(n-1) + ' W=' + str(W))
    print('    ---Exhaustive search solution ---')
    test = ""
    for i in f:
        print('       ' + str(i))
    print('       Elapsed time = ' + str(end - start) + " seconds")

if __name__ == '__main__':
    main()