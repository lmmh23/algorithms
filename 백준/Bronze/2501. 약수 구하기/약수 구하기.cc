#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

std::vector<int> findDivisors(int n) {
  std::vector<int> divisors;
  for (int i = 1; i * i <= n; i++) {
    if (n % i == 0) {
      divisors.push_back(i);
      if (i != n / i) {
        divisors.push_back(n / i);
      }
    }
  }
  std::sort(divisors.begin(), divisors.end());

  return divisors;
}

int main() {
  int n, k;
  std::cin >> n >> k;
  std::vector<int> divisors = findDivisors(n);

  std::cout << (divisors.size() < k ? "0" : std::to_string(divisors[k - 1]));
  return 0;
}