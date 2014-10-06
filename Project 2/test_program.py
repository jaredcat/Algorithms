import os


def run_file(n, W):
    os.system("python project2.py packages.txt " + str(n) + " " + str(W))


def main():
    for i in range(1, 27, 5):
        run_file(i, 2000)

if __name__ == '__main__':
    main()