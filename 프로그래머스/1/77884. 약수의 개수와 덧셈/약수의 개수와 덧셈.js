function divisorCount(num) {
  let count = 0;
  for (let i = 1; i <= num; i++) {
    if (num % i === 0) count++;
  }
  return count;
}

function solution(left, right) {
  let answer = 0;
  for (let i = left; i <= right; i++) {
    if (divisorCount(i) % 2 === 0) {
      // 짝수
      answer += i;
    } else {
      answer -= i;
    }
  }

  return answer;
}

console.log(solution(13, 17));
