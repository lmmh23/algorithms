#include <iostream>
#include <vector>

using namespace std;

struct Point {
    int x, y;
};

int main() {
    int n;
    cin >> n;

    vector<Point> points(n);

    for (int i = 0; i < n; i++) {
        cin >> points[i].x >> points[i].y;
    }

    if (n < 2) {
        cout << 0 << endl;
        return 0;
    }

    int minX = points[0].x, minY = points[0].y, maxX = points[1].x, maxY = points[1].y;

    for (const auto &p: points) {
        if (p.x < minX) { minX = p.x; }
        if (p.x > maxX) { maxX = p.x; }
        if (p.y < minY) { minY = p.y; }
        if (p.y > maxY) { maxY = p.y; }
    }

    if (minX == maxX || minY == maxY) {
        cout << 0 << endl;
        return 0;
    }
    cout << (maxX - minX) * (maxY - minY) << endl;
    return 0;
}
