#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int numToRank(int num) {
    switch (num) {
        case 6: return 1;
        case 5: return 2;
        case 4: return 3;
        case 3: return 4;
        case 2: return 5;
        default: return 6;
    }
}

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;

    int numOfDirty = 0;
    vector<int> filteredLottos;

    for (int i: lottos) {
        if (i == 0) {
            numOfDirty++;
        } else {
            filteredLottos.push_back(i);
        }
    }

    int correct = 0;
    for (int win: win_nums) {
        for (int user: filteredLottos) {
            if (win == user) {
                correct++;
                break; // 중복 방지
            }
        }
    }

    return {numToRank(correct + numOfDirty), numToRank(correct)};
}


int main() {
    solution({44, 1, 0, 0, 31, 25}, {31, 10, 45, 1, 6, 19});
    return 0;
}
