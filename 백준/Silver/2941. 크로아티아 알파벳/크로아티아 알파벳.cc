#include <iostream>
#include <string>

using namespace std;

int main() {
  string str;
  cin >> str;

  int cnt = 0;
  int i = 0;

  while (i < str.length()) {
    if (i == str.length() - 1 && str[i] >= 'a' && str[i] <= 'z') {
      cnt += 1;
      i += 1;
      continue;
    }

    if (str[i] == 'c' && (str[i + 1] == '=' || str[i + 1] == '-')) {
      cnt += 1;
      i += 2;
      continue;
    } else if (str[i] == 'd') {
      if (str[i + 1] == '-') {
        cnt += 1;
        i += 2;
        continue;
      }
      if (i != str.length() - 2 && str[i + 1] == 'z' && str[i + 2] == '=') {
        cnt += 1;
        i += 3;
        continue;
      }
    } else if ((str[i] == 'l' || str[i] == 'n') && str[i + 1] == 'j') {
      cnt += 1;
      i += 2;
      continue;
    } else if ((str[i] == 's' || str[i] == 'z') && str[i + 1] == '=') {
      cnt += 1;
      i += 2;
      continue;
    }
    cnt += 1;
    i++;
  }
  cout << cnt;
}
