function solution(k, score) {
  var answer = [];

  const candidate = [];
  for (const s of score) {
    candidate.push(s);
    candidate.sort((a, b) => a - b);
    if (candidate.length <= k) {
      answer.push(candidate[0]);
    } else {
      candidate.shift();
      answer.push(candidate[0]);
    }
  }

  console.log(answer);
  return answer;
}

solution(3, [10, 100, 20, 5, 1, 100, 200]);
solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]);