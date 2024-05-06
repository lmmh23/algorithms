#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

string alphatonum(string s) {
    string temp;
    
    for (int i = 0; i < s.length();) {
        if (s.substr(i, 3) == "one") {
            temp += '1';
            i += 3;
        }
        else if (s.substr(i, 3) == "two") {
            temp += '2';
            i += 3;
        }
        else if (s.substr(i, 3) == "six") {
            temp += '6';
            i += 3;
        }
        else if (s.substr(i, 4) == "zero") {
            temp += '0';
            i += 4;
        }
        else if (s.substr(i, 4) == "four") {
            temp += '4';
            i += 4;
        }
        else if (s.substr(i, 4) == "five") {
            temp += '5';
            i += 4;
        }
        else if (s.substr(i, 4) == "nine") {
            temp += '9';
            i += 4;
        }
        else if (s.substr(i, 5) == "three") {
            temp += '3';
            i += 5;
        }
        else if (s.substr(i, 5) == "seven") {
            temp += '7';
            i += 5;
        }
        else if (s.substr(i, 5) == "eight") {
            temp += '8';
            i += 5;
        }                                      
    }
    return temp;
}
int alphalength(string s) {
    int n = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] >= '0' && s[i] <= '9') {
            n = i;
            return n;
        }
    }
    n = s.length();
}

int solution(string s) {
    int answer = 0;
    string temp;
    for (int i = 0; i < s.length();) {
        if (s[i] >= '0' && s[i] <= '9') {
            temp += s[i];
            i++;
        }
        else if (s[i] >= 'a' && s[i] <= 'z') {
            int m = alphalength(s.substr(i));
            string n = alphatonum(s.substr(i, m));
            temp += n;
            i += m;
        }
    }
    answer = stoi(temp);
    return answer;
}