#include <bits/stdc++.h>
using namespace std;

int N;
vector<int> apeach(11);
vector<int> best(11, -1);
int maxDiff = -1;

void dfs(int idx, int remain, vector<int>& ryan) {
    if (idx == 11 || remain == 0) {
        // 남은 화살은 0점 칸에 몰아주기
        if (remain > 0) ryan[10] += remain;

        int aScore = 0, rScore = 0;
        for (int i = 0; i < 11; i++) {
            if (apeach[i] == 0 && ryan[i] == 0) continue;
            if (ryan[i] > apeach[i]) rScore += (10 - i);
            else aScore += (10 - i);
        }

        int diff = rScore - aScore;
        if (diff > 0) {
            if (diff > maxDiff) {
                maxDiff = diff;
                best = ryan;
            } else if (diff == maxDiff) {
                // 낮은 점수부터 비교
                for (int i = 10; i >= 0; i--) {
                    if (ryan[i] > best[i]) {
                        best = ryan;
                        break;
                    } else if (ryan[i] < best[i]) break;
                }
            }
        }

        if (remain > 0) ryan[10] -= remain; // 복구
        return;
    }

    // 1. 해당 점수를 이길 수 있을 경우 -> info[idx]+1 발 쏘기
    if (remain > apeach[idx]) {
        ryan[idx] = apeach[idx] + 1;
        dfs(idx + 1, remain - ryan[idx], ryan);
        ryan[idx] = 0; // backtracking
    }

    // 2. 그냥 포기하고 0발 쏘기
    dfs(idx + 1, remain, ryan);
}

vector<int> solution(int n, vector<int> info) {
    N = n;
    apeach = info;
    vector<int> ryan(11, 0);
    dfs(0, N, ryan);

    if (maxDiff <= 0) return {-1};
    return best;
}

int main() {
    vector<int> info = {2,1,1,1,0,0,0,0,0,0,0};
    int n = 5;
    auto ans = solution(n, info);
    for (int x : ans) cout << x << " ";
    cout << endl;
}
