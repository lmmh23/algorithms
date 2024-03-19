#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
  int N;
  cin >> N;

  for (int i = 1; i <= N; ++i)
  {
    cout << setw(N) << setfill(' ') << string(i, '*') << endl;
  }

  return 0;
}