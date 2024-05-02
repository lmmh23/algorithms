function solution(s) {
  var answer = 0;

  let prev = 0, cur = 0, first;
  [...s].map((str, idx) => {
    if (!first) {
      first = str;
      prev++;
    } else if (first === str) {
      prev++;
    } else {
      cur++;
    }

    if (prev === cur) {
      prev = 0;
      cur = 0;
      first = undefined;
      answer++;
    }
  })

  if (prev !== 0 || cur !== 0) {
    answer++;
  }

  console.log(answer);
  return answer;

}

solution("banana");
// solution("abracadabra");
// solution("aaabbaccccabba");