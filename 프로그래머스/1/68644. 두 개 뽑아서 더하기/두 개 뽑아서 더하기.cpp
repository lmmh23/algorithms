#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int>numbers) {
	vector<int> answer;
	vector<int> temp;
	int n;
	bool tmp = true;
	for (int i = 0; i < numbers.size(); i++) {
		for (int j = 0; j < numbers.size() - i - 1; j++) {
			n = numbers[i] + numbers[i + j + 1];
			tmp = true;
			for (int k = 0; k < answer.size(); k++) {
				if (n == answer[k]) {
					tmp = false;
					break;
				}
			}
			if (tmp == true) {
				answer.push_back(n);
			}
			else
				continue;
		}
	}
	sort(answer.begin(), answer.end(), less<int>());

	return answer;
}