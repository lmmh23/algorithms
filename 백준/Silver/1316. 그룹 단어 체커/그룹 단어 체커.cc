#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isGroupWord(const string& word) {
  bool visited[26] = {false};
  char prev = '\0';

  for (char ch : word) {
    if (ch != prev) {
      if (visited[ch - 'a']) {
        return false;
      }
      visited[ch - 'a'] = true;
    }
    prev = ch;
  }

  return true;
}

int main() {
  int n;
  int cnt = 0;
  cin >> n;

  vector<string> words;
  string word;

  for (int i = 0; i < n; i++) {
    cin >> word;
    if (isGroupWord(word)) cnt++;
  }
  cout << cnt;
}
