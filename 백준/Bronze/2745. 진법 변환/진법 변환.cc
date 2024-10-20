#include <iostream>
#include <vector>

using namespace std;

int main() {
  string str_b;
  int N;
  int sum = 0;
  cin >> str_b >> N;

  for (int i = 0; i < str_b.length(); i++) {
    if ('0' <= str_b[i] && str_b[i] <= '9') {
      sum = sum * N + (str_b[i] - '0');
    } else {
      sum = sum * N + (str_b[i] - 'A' + 10);
    }
  }
  cout << sum;

  return 0;
}