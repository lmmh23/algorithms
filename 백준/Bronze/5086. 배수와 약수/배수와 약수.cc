 #include <iostream>

int main() {
  while (true) {
    int n, m;

    std::cin >> n >> m;
    if (n == 0 && m == 0) {
      break;
    } else if (m % n == 0) {
      std::cout << "factor" << std::endl;
    } else if (n % m == 0) {
      std::cout << "multiple" << std::endl;
    } else {
      std::cout << "neither" << std::endl;
    }
  }
}