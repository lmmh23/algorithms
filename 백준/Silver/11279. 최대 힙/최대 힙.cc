#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main() {    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    vector<int> answer;

    int N, temp;
    cin >> N;
    priority_queue<int> Maxheap;

    for (int i = 0; i < N; i++) {
        cin >> temp;
        if (temp != 0) {
            Maxheap.push(temp);
        }
        else {
            if (Maxheap.empty()) {
                answer.push_back(0);
            }
            else {
                answer.push_back(Maxheap.top());
                Maxheap.pop();
            }
        }
    }

    for (int i = 0; i < answer.size(); i++)
        cout << answer[i] << '\n';

    return 0;
}