#include <string>
#include <vector>

using namespace std;

int solution(vector<int> players, int m, int k) {
    int n = players.size();
    vector<int> activeServers(n, 0); // 각 시간대에 새로 증설한 서버 수 기록
    int totalAdditions = 0;

    for (int hour = 0; hour < n; ++hour) {
        // 지난 k시간 동안 운영 중인 서버 수 계산
        int currentActive = 0;
        for (int t = max(0, hour - k + 1); t <= hour; ++t) {
            currentActive += activeServers[t];
        }

        // 현재 시간대에 필요한 서버 수
        int required = 0;
        if (players[hour] >= m) {
            required = players[hour] / m; // 서버 1대당 m명 처리
        }

        // 서버 증설 필요 시
        if (required > currentActive) {
            int add = required - currentActive;
            activeServers[hour] = add;
            totalAdditions += add;
        }
    }

    return totalAdditions;
}