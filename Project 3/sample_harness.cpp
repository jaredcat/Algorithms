
#include <chrono>
#include <iostream>

using namespace std;

void replace_this_with_a_real_algorithm() {
  // waste time...
  const int N = 1 << 15;
  for (int i = 0; i < N; ++i)
    for (int j = 0; j < N; ++j)
      ;
}

int main(int argc, char** argv) {
  cout << "running algorithm..." << endl;
  auto start = chrono::high_resolution_clock::now();
  replace_this_with_a_real_algorithm();
  auto end = chrono::high_resolution_clock::now();

  int microseconds = chrono::duration_cast<chrono::microseconds>(end - start).count();
  double seconds = microseconds / 1E6;
  cout << "elapsed time: " << seconds << " seconds" << endl;

  return 0;
}
