#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

double gradeToPoint(const string& grade) {
  if (grade == "A+")
    return 4.5;
  else if (grade == "A0")
    return 4.0;
  else if (grade == "B+")
    return 3.5;
  else if (grade == "B0")
    return 3.0;
  else if (grade == "C+")
    return 2.5;
  else if (grade == "C0")
    return 2.0;
  else if (grade == "D+")
    return 1.5;
  else if (grade == "D0")
    return 1.0;
  else if (grade == "F")
    return 0.0;
  else if (grade == "P")
    return 0.0;  // Pass는 GPA에 포함되지 않음
  return 0.0;    // 기본값
}

int main() {
  vector<string> lines;
  string line;

  for (int i = 0; i < 20; i++) {
    getline(cin, line);

    if (line.empty()) {
      break;
    }
    lines.push_back(line);
  }

  double totalCredits = 0;
  double totalGrade = 0;

  for (const string& l : lines) {
    string course, grade;
    double credits;

    istringstream iss(l);

    iss >> course;
    iss >> credits >> grade;

    if (grade == "P") {
      continue;
    }

    totalCredits += credits;
    totalGrade += credits * gradeToPoint(grade);
  }

  if (totalGrade == 0) {
    cout << "0.000000";
  } else {
    cout << fixed << setprecision(6);
    cout << totalGrade / totalCredits;
  }
}
