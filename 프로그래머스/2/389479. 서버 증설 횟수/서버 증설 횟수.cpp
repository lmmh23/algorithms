#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int solution(vector<int> players, int m, int k) {
    int answer = 0;
    vector<int> activatedServers(24, 0);
    int activeServer = 0;

    for (int i = 0; i < players.size(); i++) {
        if (i >= k) {
            activeServer -= activatedServers[i - k];
        }


        int requiredServer = players[i] / m;

        cout << "requiredServer: " << requiredServer << " activatedServer" << activeServer << endl;

        if (requiredServer > activeServer) {
            int add = requiredServer - activeServer;
            activeServer += add;
            answer += add;
            activatedServers[i] = add;
        }
    }

    cout << answer << endl;

    return answer;
}

int main() {
    solution({0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5}, 3, 5);
    return 0;
}
