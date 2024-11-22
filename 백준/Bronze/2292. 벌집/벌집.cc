#include <iostream>

int main() {
  int n;
  std::cin >> n;
  /**
   * 1 (1), 2~7 (6), 8~19 (12), 20~37 (18), 38~61 (24)
   */
  int layer = 1;
  int count = 1;
  while (n > count) {
    count += 6 * layer++;
  }

  std::cout << layer;

  return 0;
}