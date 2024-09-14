#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
  string a, b;
  cin >> a >> b;

  reverse(a.begin(), a.end());
  reverse(b.begin(), b.end());

  int numA = stoi(a);
  int numB = stoi(b);

  if (numA > numB) {
    cout << numA << endl;
  } else {
    cout << numB << endl;
  }
  return 0;
}