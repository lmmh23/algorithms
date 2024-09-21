#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  const int ALPHABET_COUNT = 26;

  vector<int> alphabet(ALPHABET_COUNT, 0);

  string str;
  cin >> str;

  for (int i = 0; i < str.length(); i++) {
    alphabet[(str[i] >= 65 && str[i] <= 90) ? str[i] + 32 - 'a'
                                            : str[i] - 'a']++;
  }

  int maxValue = alphabet[0];

  for (int i = 1; i < alphabet.size(); i++) {
    if (alphabet[i] > maxValue) {
      maxValue = alphabet[i];
    }
  }

  vector<int> maxIndexes;

  for (int i = 0; i < alphabet.size(); i++) {
    if (alphabet[i] == maxValue) {
      maxIndexes.push_back(i);
    }
  }

  cout << (maxIndexes.size() >= 2 ? '?' : char(maxIndexes[0] + 'A'));
}
