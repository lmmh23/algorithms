#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

vector<int> solution(vector<string> id_list, vector<string> report, int k) {
	vector<int> answer;
	answer.assign(id_list.size(), 0);

	vector<string> id;	
	id.assign(id_list.begin(), id_list.end());

	set<string> s(report.begin(), report.end());	
	vector<string> set_report(s.begin(), s.end());

	vector<int> reported(id.size(), 0);

	for (int i = 0; i < set_report.size(); i++) {
		if (set_report[i].find(" ") != string::npos) {
			auto it = find(id.begin(), id.end(), set_report[i].substr(set_report[i].find(" ") + 1));
			++reported[it - id.begin()];
		}
	}

	vector<int> temp;
	for (int i = 0; i < reported.size(); i++) {
		if (reported[i] >= k) {	//신고 횟수가 k번 이상인 사람들의 index 가져오기
			temp.push_back(i);
		}
	}

	for (int i = 0; i < set_report.size(); i++) {		//신고한 사람에게 메일 날리기
		for (int j = 0; j < temp.size(); j++) {
			if (set_report[i].find(id[temp[j]], set_report[i].find(" ")) != string::npos) {
				auto itor = find(id.begin(), id.end(), set_report[i].substr(0, set_report[i].find(id[temp[j]]) - 1));
				++answer[itor - id.begin()];
				break;
			}
		}
	}
    return answer;
}
