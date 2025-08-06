#include <iostream>

using namespace std;

int solution(int n, int w, int num) {
  int row = (num - 1) / w; // 층수 0부터 시작
  int col;
  if (row % 2 == 0) {
    col = (num - 1) % w; // 짝수층은 왼쪽에서 오른쪽으로
  } else {
    col = w - 1 - (num - 1) % w; // 홀수층은 오른쪽에서 왼쪽으로
  }

  cout << "row: " << row << ", col: " << col << endl;

  int answer = 0;

  for (int i = row; i <= (n - 1) / w; i++) {
    int boxNum;
    if (i % 2 == 0) {
      boxNum = i * w + (col + 1);
    } else {
      boxNum = i * w + (w - col);
    }
    if (boxNum > n) {
      break;
    }
    answer++;
    cout << "boxNum: " << boxNum << endl;
  }

  return answer;
}