#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main() {
  string str;

  cin >> str;

  int leng = str.length();

  string a = str.substr(0, leng / 2);
  string b = str.substr(leng % 2 == 0 ? leng / 2 : leng / 2 + 1);

  reverse(b.begin(), b.end());

  if (a == b) {
    cout << 1;
  } else {
    cout << 0;
  }
}
