#include <cmath>
#include <iostream>

int main() {
  int x;
  std::cin >> x;

  int i = 1;
  while (x > i) {
    x -= i++;
  }

  if (i % 2 == 0) {
    std::cout << x << "/" << i - x + 1;
  } else {
    std::cout << i - x + 1 << "/" << x;
  }

  return 0;
}