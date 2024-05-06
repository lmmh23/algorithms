#include <string>
#include <vector>

using namespace std;
string solution(string s, int n) {
string answer = "";
	int i = 0;
	int j = 0;
	while (j < s.length()) {
		if (s[i] >= 'a' && s[i] <= 'z') {
			if (s[i] + n > 'z') {
				answer += s[i] + n - ('z' - 'a' + 1);
			}
			else {
				answer += s[i] + n;
			}
		}
		else if (s[i] >= 'A' && s[i] <= 'Z') {
			if (s[i] + n > 'Z') {
				answer += s[i] + n - ('Z' - 'A' + 1);
			}
			else {
				answer += s[i] + n;
			}
		}
		else if (s[i] == ' ') {
			answer += " ";
		}
        i++;
        j++;
    }
	return answer;
}