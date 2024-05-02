#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool CanSkillTree(string skill, string skill_tree) {
    vector<pair<int, int>> v;

    for (int i = 0; i < skill.size(); i++) {
        if (skill_tree.find(skill[i]) != string::npos) {
            int n = skill_tree.find(skill[i]);
            v.push_back(make_pair(n, i));
        }
    }

    if (v.empty()) return true;

    if (v[0].second != 0) return false;
    
    for (int i = 0; i < v.size()-1; i++) {
        if (v[i + 1].second != v[i].second + 1) return false;
    }
    for (int i = 0; i < v.size() - 1; i++) {
        for (int j = i + 1; j < v.size(); j++) {
            if (v[i].first > v[j].first) return false;
        }
    }
    return true;

}
int solution(string skill, vector<string> skill_trees) {
    int answer = 0;
    for (int i = 0; i < skill_trees.size(); ++i) {
        if (CanSkillTree(skill, skill_trees[i])) answer++;
    }
        
    return answer;
}