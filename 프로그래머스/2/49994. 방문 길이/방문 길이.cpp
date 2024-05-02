#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string dirs) {
    int answer = 0;
    // fromX, fromY, toX, toY
    int board[11][11][11][11] = { 0, };

    int idx = 0;
    int dirsLen = (int)dirs.length();

    int curX = 5;
    int curY = 5;

    while (idx < dirsLen){
        char dir = dirs[idx];
        if (dir == 'U') {
            if (curY + 1 < 11) {
                if (board[curX][curY][curX][curY + 1] != 1) {
                    board[curX][curY][curX][curY + 1] = 1;
                    board[curX][curY + 1][curX][curY] = 1;
                    answer++;
                }
                curY++;
            }
        }
        else if (dir == 'D') {
            if (curY - 1 >= 0) {
                if (board[curX][curY][curX][curY - 1] != 1) {
                    board[curX][curY][curX][curY - 1] = 1;
                    board[curX][curY - 1][curX][curY] = 1;
                    answer++;
                }
                curY--;
            }
        }
        else if (dir == 'L') {
            if (curX - 1 >= 0) {
                if (board[curX][curY][curX - 1][curY] != 1) {
                    board[curX][curY][curX - 1][curY] = 1;
                    board[curX - 1][curY][curX][curY] = 1;
                    answer++;
                }
                curX--;
            }
        }
        else if (dir == 'R') {
            if (curX + 1 < 11) {
                if (board[curX][curY][curX + 1][curY] != 1) {
                    board[curX][curY][curX + 1][curY] = 1;
                    board[curX + 1][curY][curX][curY] = 1;
                    answer++;
                }
                curX++;
            }
        }

        idx++;
    }

    return answer;
}