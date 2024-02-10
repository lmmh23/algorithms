#include <iostream>

using namespace std;

int main() {
  int byte;
  cin >> byte;

  while(byte) {
    cout << "long ";
    byte -= 4;
  }
  cout << "int";
}