#include <iostream>
#include <vector>

bool isPrime(int n) {
  for (int i = 2; i < n; i++) {
    if (n % i == 0) return false;
  }
  return true;
}

int main() {
  int m;
  std::cin >> m;
  int n;
  std::cin >> n;
  std::vector<int> primes;
  int sum = 0;

  for (int i = m; i <= n; i++) {
    if (i != 1 && isPrime(i)) {
      primes.push_back(i);
      sum += i;
    }
  }

  if (primes.size() == 0) {
    std::cout << "-1";
  } else {
    std::cout << sum << std::endl << primes[0];
  }

  return 0;
}