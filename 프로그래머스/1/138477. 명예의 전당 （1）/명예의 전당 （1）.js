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