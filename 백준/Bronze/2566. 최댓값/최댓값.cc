#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
  int N = 9, M = 9;

  vector<vector<int>> A(9, vector<int>(9));

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      cin >> A[i][j];
    }
  }

  int max = -1;
  int row, col;

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      if (max < A[i][j]) {
        max = A[i][j];
        row = i + 1;
        col = j + 1;
      }
    }
  }

  cout << max << endl;
  cout << row << " " << col;

  return 0;
}
