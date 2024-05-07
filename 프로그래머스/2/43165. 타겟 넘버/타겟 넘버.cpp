#include <iostream>
#include <vector>
#include <string>

using namespace std;

int answer = 0;

void BFS(vector<int> numbers, int target, int sum, int index) {

	if (index == numbers.size()) {
		if (sum == target) answer++;
		return;
	}

	BFS(numbers, target, sum + numbers[index], index + 1);
	BFS(numbers, target, sum - numbers[index], index + 1);

}
int solution(vector<int> numbers, int target) {
	BFS(numbers, target, 0, 0);

	return answer;
}