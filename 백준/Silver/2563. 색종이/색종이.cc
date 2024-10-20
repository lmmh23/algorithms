#include <iostream>
#include <vector>

using namespace std;

int main() {
  bool paper[100][100] = {0};
  int sum = 0;

  int N;
  cin >> N;

  for (int i = 0; i < N; i++) {
    int x, y;
    cin >> x >> y;
    for (int j = y; j < y + 10; j++) {
      for (int z = x; z < x + 10; z++) {
        if (paper[j][z]) continue;
        paper[j][z] = 1;
        sum++;
      }
    }
  }
  cout << sum;
  return 0;
}