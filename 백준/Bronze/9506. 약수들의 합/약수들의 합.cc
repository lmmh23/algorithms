#include <algorithm>
#include <iostream>
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
  while (true) {
    int n;
    std::cin >> n;
    if (n == -1) {
      break;
    }
    std::vector<int> divisors = findDivisors(n);
    int sum = 0;
    for (auto &it : divisors) {
      if (it != n) {
        sum += it;
      }
    }

    if (sum == n) {
      std::cout << n << " = ";
      for (int i = 0; i < divisors.size() - 1; i++) {
        std::cout << divisors[i] << (i != divisors.size() - 2 ? " + " : "\n");
      }
    } else {
      std::cout << n << " is NOT perfect." << std::endl;
    }
  }
  return 0;
}