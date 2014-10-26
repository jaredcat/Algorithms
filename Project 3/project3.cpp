#include <chrono>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void read_file(string *list, string filename, int n){
	ifstream infile;
	infile.open(filename);
	for (int i = 0; i < n; i++){
		getline(infile, list[i]);
	}
	infile.close();
}


void first_ten(string *list, int n){
	if (n > 10)
		n = 10;
	cout << "First " << n << " words: ";
	for (int i=0; i < n; i++){
		cout << "[" << list[i] << "] ";
	}
	cout << endl;
}


void selection_sort(string *l, int n) {
    int min_l = 0;
    if (n < 2){
		return;
    }else{
		for (int i = 0; i < n - 1; ++i){
			for (int j = i + 1; j < n; ++j){
				if (l[j] < l[min_l])
					min_l = j;
			}
			if (min_l != i)
				swap(l[i], l[min_l]);
		}
    }
}


void swap(string *a, string *b){
	string swap;
	swap = *a;
	*a = *b;
	*b = swap;
}


int main(int argc, char* argv[]) {
	if (argc != 3){
		cout << "error: you must supply exactly three arguments" << endl << endl << 
			"usage: <program exe> <text file> <n>";
		return 1;
	}

	string filename = string(argv[1]);
	int n = atoi(argv[2]);
	string * input_list;
	input_list = new string [n];

	read_file(input_list, filename, n);

	cout << "Requested n = " << n << endl;
	cout << "Loaded " << n << " line from '" << filename << "'" << endl;
	first_ten(input_list, n);

    cout << "Selection Sort [O(n2)]..." << endl;
    auto start = chrono::high_resolution_clock::now();
    selection_sort(input_list, n);
    auto end = chrono::high_resolution_clock::now();
	first_ten(input_list, n);
    int microseconds = chrono::duration_cast<chrono::microseconds>(end - start).count();
    double seconds = microseconds / 1E6;
    cout << "elapsed time: " << seconds << " seconds" << endl;

    return 0;
}