#include <algorithm>
#include <iostream>

int main() {
  int n, b;
  std::cin >> n >> b;

  std::string b_num;
  while (n != 0) {
    int tmp = n % b;
    if (tmp > 9) {
      tmp = tmp - 10 + 'A';
      b_num += tmp;
    } else {
      b_num += ('0' + tmp);
    }
    // std::cout << b_num << std::endl;
    n /= b;
  }
  std::reverse(b_num.begin(), b_num.end());

  std::cout << b_num << std::endl;

  return 0;
}