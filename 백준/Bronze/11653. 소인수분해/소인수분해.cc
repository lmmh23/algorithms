#include <iostream>

int main() {
  int n;
  std::cin >> n;

  if (n == 1) {
    return 0;
  }

  for (int i = 2; i <= n; i++) {
    while (n % i == 0) {
      std::cout << i << std::endl;
      n /= i;
    }
  }

  return 0;
}