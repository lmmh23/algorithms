#include <iostream>

using namespace std;

int main() {
  int total, numItems;

  cin >> total;
  cin >> numItems;

  int calculated = 0;

  for (int i = 0; i < numItems; i++) {
    double price;
    int quantity;
    cin >> price >> quantity;
    calculated += price * quantity;
  }

  if (calculated == total) {
    cout << "Yes";
  } else {
    cout << "No";
  }
  return 0;
}