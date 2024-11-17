#include <iostream>

int main() {
  int N;
  int dot = 2;

  std::cin >> N;

  while (N--) {
    dot = 2 * dot - 1;
  }
  std::cout << dot * dot;
  return 0;
}