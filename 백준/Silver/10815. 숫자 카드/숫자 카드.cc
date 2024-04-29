#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main(void) {
    int N,M;
    map<int, int> m;
    int temp;
    cin >> N;
    for(int i=0; i<N; i++) {
        cin >> temp;
        m[temp] = 1;
    }

    cin >> M;
    vector<int> answer(M, 0);
    for(int i=0; i<M; i++) {
        cin >> temp;
        if(m[temp] == 1) {
            answer[i] = 1;
        }
        else {
            answer[i] = 0;
        }
    }

    for(int i=0; i<M; i++) cout << answer[i] << " ";
    
    return 0;
}