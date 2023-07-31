function solution(a, b, n) {
  var answer = 0;

  while (n >= a) {
    answer += Math.floor(n / a) * b;
    n = Math.floor(n / a) + n%a;
  }


  return answer;
}

solution(2, 1, 20);
solution(3, 1, 20);