#include <iostream>

int main() {
  int T;
  std::cin >> T;
  int rest[4] = {25, 10, 5, 1};

  for (int i = 0; i < T; i++) {
    int C;
    std::cin >> C;
    for (int j = 0; j < 4; j++) {
      std::cout << C / rest[j] << " ";
      C -= (C / rest[j]) * rest[j];
    }
    std::cout << std::endl;
  }

  return 0;
}