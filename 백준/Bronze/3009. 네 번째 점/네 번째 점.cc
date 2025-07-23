#include <iostream>
#include <vector>

using namespace std;

struct Point {
    int x, y;
};

int main() {
    vector<Point> points(3);

    for (int i = 0; i < 3; i++) {
        cin >> points[i].x >> points[i].y;
    }

    int x4, y4;

    // x 좌표 찾기
    if (points[0].x == points[1].x) x4 = points[2].x;
    else if (points[0].x == points[2].x) x4 = points[1].x;
    else x4 = points[0].x;

    // y 좌표 찾기
    if (points[0].y == points[1].y) y4 = points[2].y;
    else if (points[0].y == points[2].y) y4 = points[1].y;
    else y4 = points[0].y;

    cout << x4 << " " << y4 << endl;

    return 0;
}
