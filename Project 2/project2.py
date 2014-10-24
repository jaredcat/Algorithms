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
    i = 0
    with open(file, "r") as f:
            pkg_list = []
            next(f)
            for line in f:
                    if i == n:
                        break
                    line = line.split(" ")
                    new_pkg = DebianPackage(line[0], int(line[1]), int(line[2]))
                    pkg_list.append(copy.deepcopy(new_pkg))
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


def verify_knapsack(candidate, W):
    weight_sum = 0
    for x in candidate:
        weight_sum += x.size
    if weight_sum > W:
        return 0
    else:
        return weight_sum


def compare_knapsack(candidate, best_votes):
    candidate_votes = 0
    for x in candidate:
        candidate_votes += x.votes
    if candidate_votes <= best_votes:
        return 0
    else:
        return candidate_votes


def exhaustive_knapsack(package_list, W):
    best = []
    best_votes = 0
    best_size = 0
    for candidate in subsets(package_list):
        candidate_size = verify_knapsack(candidate, W)
        if candidate_size:
            candidate_votes = compare_knapsack(candidate, best_votes)
            if candidate_votes:
                best = candidate
                best_size = candidate_size
                best_votes = candidate_votes
    return best, best_size, best_votes


def main():
    if len(sys.argv) != 4:
        print('error: you must supply exactly two arguments\n\n' +
              'usage: python3 <Python source code file> <text file> <n> <W>')
        sys.exit(1)

    filename = sys.argv[1]
    n = int(sys.argv[2])
    W = int(sys.argv[3])

    pkg_list = read_packages(filename, n)

    start = time.perf_counter()
    f = exhaustive_knapsack(pkg_list, W)
    end = time.perf_counter()
    print('------ n=' + str(n) + ' W=' + str(W))
    print('    --- Exhaustive search solution ---')
    #for i in f[0]:
        #print('        ' + str(i))
    print('        Total size=' + str(f[1]) + "  Total votes=" + str(f[2]))
    #print('        Elapsed time = ' + "{0:.2f}".format(round(end - start, 2)) + " seconds")
    print('        Elapsed time = ' + str(end - start) + " seconds")

if __name__ == '__main__':
    main()