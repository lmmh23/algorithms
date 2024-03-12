#include <iostream>

using namespace std;

int main()
{
  int N;
  cin >> N;

  for (int i = 0; i < N; i++)
  {
    int x, y;
    cin >> x >> y;

    int sum = x + y;
    cout << "Case #" << i + 1 << ": " << x << " + " << y << " = " << sum << endl;
  }

  return 0;
}