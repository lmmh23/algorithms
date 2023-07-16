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


function otherSolution(s) {
  let answer = 0;
  let current;
  let count = 0;

  // 변수 하나로 처리하기
  for(let i = 0; i < s.length; i++) {
      if(count === 0) {
          answer++;
          current = s[i]
          count = 1
      } else {
          if(current !== s[i]) count--;
          else count++;
      }
  }

  return answer;
}