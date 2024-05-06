#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<vector<int>> v(commands.size());
    for (int i = 0; i < commands.size(); i++) {
        for (int j = 0; j < commands[i][1] - commands[i][0] + 1; j++) {
            v[i].push_back(array[commands[i][0] - 1 + j]);
        }
        sort(v[i].begin(), v[i].end(), less<int>());
        answer.push_back(v[i][commands[i][2] - 1]);
    }
    return answer;
}