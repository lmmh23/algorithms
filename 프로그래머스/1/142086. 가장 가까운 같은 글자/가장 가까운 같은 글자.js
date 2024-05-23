function solution(s) {
  var answer = [];

  // map은 해당 알파벳이 나왔었는지를 체크.
  var map = {};
  for (let i = 0; i<s.length; i++) {
    if (map[s[i]] === undefined) {
      // 해당 알파벳이 한번도 나온 적 없으면
      map[s[i]] = i;
      answer.push(-1);
    } else {
      answer.push(i - map[s[i]]);
      map[s[i]] = i;
    }
  }
  console.log(answer);
  return answer;
}

solution("banana");