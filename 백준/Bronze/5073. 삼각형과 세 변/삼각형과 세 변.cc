#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int a, b, c;

    while (true) {
        cin >> a >> b >> c;
        if (a == 0 && b == 0 && c == 0) { break; }

        int maxSide = max(a, max(b, c));
        int sumOther = a + b + c - maxSide;

        if (maxSide >= sumOther) {
            cout << "Invalid" << endl;
        } else if (a == b && b == c && c == a) {
            cout << "Equilateral" << endl;
        } else if (a == b || b == c || c == a) {
            cout << "Isosceles" << endl;
        } else {
            cout << "Scalene" << endl;
        }
    }

    return 0;
}
