#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int addMinutes(int time, int addMin) {
    int hour = time / 100;
    int minute = time % 100;

    minute += addMin;

    while (minute >= 60) {
        minute -= 60;
        hour++;
    }
    return hour * 100 + minute;
}

int solution(vector<int> schedules, vector<vector<int> > timelogs, int startday) {
    int answer = 0;
    const int MAX_WEEKDAYS = 7;

    for (int i = 0; i < timelogs.size(); i++) {
        int schedule = addMinutes(schedules[i], 10);
        int copied = startday;

        bool isSuccess = true;

        for (int j = 0; j < timelogs[i].size(); j++) {
            if (copied > 5) {
                copied = copied % MAX_WEEKDAYS + 1;
                continue;
            }
            if (schedule < timelogs[i][j]) {
                isSuccess = false;
            }

            copied = (copied + 1) % MAX_WEEKDAYS;
        }

        if (isSuccess) {
            answer++;
        }
    }

    cout << answer << endl;

    return answer;
}

int main() {
    solution({700, 800, 1100}, {
                 {710, 2359, 1050, 700, 650, 631, 659}, {800, 801, 805, 800, 759, 810, 809},
                 {1105, 1001, 1002, 600, 1059, 1001, 1100}
             }, 5);
    return 0;
}
