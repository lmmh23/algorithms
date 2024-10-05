#include <iostream>
#include <vector>

using namespace std;

int main() {
  vector<vector<char>> matrix;
  string line;

  int maxLength = 0;

  for (int i = 0; i < 5; i++) {
    cin >> line;
    vector<char> row(line.begin(), line.end());
    matrix.push_back(row);

    if (line.size() > maxLength) {
      maxLength = line.size();
    }
  }

  for (int col = 0; col < maxLength; col++) {
    for (int row = 0; row < matrix.size(); row++) {
      if (col < matrix[row].size()) {
        cout << matrix[row][col];
      }
    }
  }

  return 0;
}