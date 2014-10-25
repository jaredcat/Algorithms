import time
import sys

def read_file(filename,n):
    i = 0
    word_list = []
    with open(filename, "r") as f:
        for line in f:
            if i == n:
                break
            line = line.split("\n")
            word_list.append(line[0])
            i += 1
    return word_list


def first_ten(input_list):
    ten = []
    for i in input_list[0:10]:
        ten.append(i)
    return ten


def selection_sort(l):
    min_l = 0
    if len(l) < 2:
        return l
    else:
        for i in range(0, len(l)-1):
            for j in range(i+1, len(l)):
                if l[j] < l[min_l]:
                    min_l = j
            if min_l != i:
                l[i], l[min_l] = l[min_l], l[i]
    return l


def merge_sort(l):
    if len(l) < 2:
        return l
    else:
        half = int(len(l)/2)
        left = l[:half]
        right = l[half:]
        solution_left = merge_sort(left)
        solution_right = merge_sort(right)
        solution_l = merge(solution_left, solution_right)
    return solution_l


def merge(left, right):
    merged = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            x = left[l]
            l += 1
        else:
            x = right[r]
            r += 1
        merged.append(x)
    return merged + left[l:] + right[r:]


def main():
    if len(sys.argv) != 4:
        print('error: you must supply exactly two arguments\n\n' +
              'usage: python3 <Python source code file> <text file> <n> <selection||merge>')
        sys.exit(1)

    filename = sys.argv[1]
    n = int(sys.argv[2])
    sort_type = sys.argv[3]

    input_list = read_file(filename, n)

    print('Requested n = ' + str(n))
    print('Loaded ' + str(n) + ' lines from "' + filename + '"')
    print('First 10 words: ' + str(first_ten(input_list)))

    if sort_type == "selection":
        print('Selection Sort [O(n^2)]...')
        start = time.perf_counter()
        sorted_list = selection_sort(input_list)
        end = time.perf_counter()
    elif sort_type == "merge":
        print('Merge Sort [O(nlogn)]...')
        start = time.perf_counter()
        sorted_list = merge_sort(input_list)
        end = time.perf_counter()

    print('First 10 words: ' + str(first_ten(sorted_list)))
    print('Elapsed time: ' + str(end-start) + " seconds")

if __name__ == '__main__':
    main()