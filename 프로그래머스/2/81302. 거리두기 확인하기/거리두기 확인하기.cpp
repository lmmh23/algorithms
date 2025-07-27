#include <string>
#include <vector>
#include <queue>

using namespace std;

int xmoving[4] = {0, 1, 0, -1};
int ymoving[4] = {1, 0, -1, 0};

vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;

    for (int seq = 0; seq < 5; ++seq) {  // 각 대기실(5개)에 대해 검사
        bool isSafe = true;

        for (int x = 0; x < 5 && isSafe; ++x) {
            for (int y = 0; y < 5 && isSafe; ++y) {
                if (places[seq][x][y] != 'P') continue;

                // BFS 시작
                int chk[5][5] = {0};
                queue<pair<int, int>> q;
                chk[x][y] = 1;
                q.push({x, y});

                while (!q.empty() && isSafe) {
                    auto [now_x, now_y] = q.front();
                    q.pop();

                    if (chk[now_x][now_y] >= 3) continue;

                    for (int i = 0; i < 4; i++) {
                        int tx = now_x + xmoving[i];
                        int ty = now_y + ymoving[i];

                        if (tx < 0 || ty < 0 || tx >= 5 || ty >= 5) continue;
                        if (chk[tx][ty] || places[seq][tx][ty] == 'X') continue;

                        if (places[seq][tx][ty] == 'P') {
                            isSafe = false; // 거리두기 위반
                            break;
                        }

                        chk[tx][ty] = chk[now_x][now_y] + 1;
                        q.push({tx, ty});
                    }
                }
            }
        }

        answer.push_back(isSafe ? 1 : 0);
    }

    return answer;
}
