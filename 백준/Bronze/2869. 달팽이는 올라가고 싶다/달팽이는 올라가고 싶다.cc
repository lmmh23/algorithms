#include <iostream>

int main() {
  int a, b, v;
  std::cin >> a >> b >> v;

  int day = 1;
  day += (v - a) / (a - b);
  if ((v - a) % (a - b) != 0) day++;
  if (a >= v)
    std::cout << "1";
  else
    std::cout << day;
  return 0;
}