#include <string>
#include <vector>
#include <iostream>
#include <unordered_set>

using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    unordered_set<string> seen;

    for (int i = 0; i < words.size(); i++) {
        bool isFirstIndex = i == 0;
        const string &prevWord = words[i - 1];
        const string &curWord = words[i];

        bool isExist = seen.find(curWord) != seen.end();
        if (!isExist) {
            seen.insert(curWord);
        }
        bool failed = isFirstIndex ? false : prevWord[prevWord.length() - 1] != curWord[0];

        if (isExist || failed) {
            answer.push_back((i + 1) % n == 0 ? n : (i % n) + 1);
            answer.push_back(i / n + 1);
            break;
        }
    }

    return !answer.empty() ? answer : vector<int>{0, 0};
}
