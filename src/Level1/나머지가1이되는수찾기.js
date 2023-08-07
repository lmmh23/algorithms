function solution(n) {
  /** 
   * n을 x로 나눈 나머지가 1인 x 중 가장 작은 숫자.
   * n % x == 1
  */
  for (let i = 1; i < n; i++) {
    if (n % i === 1) {
      return i;
    }
  }
}

console.log(solution(10));
console.log(solution(12));
