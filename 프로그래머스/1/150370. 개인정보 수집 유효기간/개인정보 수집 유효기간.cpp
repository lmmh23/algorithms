#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(string today, vector<string> terms, vector<string> privacies) {
    vector<int> answer;
    map<string, int> termMap;

    const int MAX_DAYS = 28;
    const int MAX_MONTHS = 12;

    for (const auto &term: terms) {
        const size_t pos = term.find(' ');
        string termType = term.substr(0, pos);
        string graceDays = term.substr(pos + 1);

        termMap[termType] = stoi(graceDays);
    }

    for (int i = 0; i < privacies.size(); i++) {
        string privacy = privacies[i];
        int pos = privacy.find(' ');
        string date = privacy.substr(0, pos);
        string termType = privacy.substr(pos + 1);

        int pos1 = date.find('.');
        int pos2 = date.find('.', pos1 + 1);
        int year = stoi(date.substr(0, pos1));
        int month = stoi(date.substr(pos1 + 1, pos2 - pos1 - 1));
        string day = date.substr(pos2 + 1);

        int newMonth = (month + termMap[termType] - 1) % MAX_MONTHS + 1;
        int newYear = year + (month + termMap[termType] - 1) / MAX_MONTHS;


        string newDate = to_string(newYear) + "." + (newMonth < 10
                                                         ? "0" + to_string(newMonth)
                                                         : to_string(newMonth)) + "." + day;

        if (newDate <= today) {
            answer.push_back(i + 1);
        }

        cout << newDate << endl;

        // int newDay = (day + termMap[termType]) % MAX_DAYS;
        // int newMonth = (month + (day + termMap[termType]) / MAX_DAYS) % MAX_MONTHS;
        // int newYears = year + (month + (day + termMap[termType]) / MAX_DAYS) / MAX_MONTHS;
        //
        // string newDate = to_string(newYears) + "." + to_string(newMonth) + "." + to_string(newDay);
    }

    for (const auto &a: answer) {
        cout << a << endl;
    }

    return answer;
}

int main() {
    // solution("2022.05.19", {"A 6", "B 12", "C 3"},
    //          {"2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"});
    // solution("2020.01.01", )
    solution("2020.04.16", {"A 36", "S 4"}, {"2017.04.17 A", "2014.04.16 S"});
    return 0;
}
