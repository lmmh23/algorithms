#include <iostream>

bool isPrime(int n) {
  for (int i = 2; i < n; i++) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}

int main() {
  int n;
  std::cin >> n;
  int cnt = 0;
  for (int i = 0; i < n; i++) {
    int k;
    std::cin >> k;
    if (k != 1 && isPrime(k)) cnt++;
  }
  std::cout << cnt;

  return 0;
}