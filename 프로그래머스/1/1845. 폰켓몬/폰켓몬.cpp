#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> nums) {
	int answer = 0;
	int i = 0;
	answer = nums.size() / 2;
	vector<int> temp;
	temp = nums;
	sort(temp.begin(), temp.end(), less<int>());
	for (int i = 0; i < temp.size()-1;) {
		if (temp[i] == temp[i + 1]) {
			temp.erase(temp.begin() + i+1);
		}
        else
            i++;
	}
	if (temp.size() >= answer) return answer;
	else {
		answer -= (nums.size()/2) - temp.size();
	}
	return answer;
}