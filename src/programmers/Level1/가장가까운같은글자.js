function solution(s) {
  var answer = [];

  // map은 해당 알파벳이 나왔었는지를 체크.
  var map = {};
  for (let i = 0; i<s.length; i++) {
    console.log(map);
    if (map[s[i]] === undefined) {
      // 해당 알파벳이 한번도 나온 적 없으면
      map[s[i]] = i;
      answer.push(-1);
    } else {
      answer.push(i - map[s[i]]);
      map[s[i]] = i;
    }
  }
  // console.log(answer);
  return answer;
}

solution("aaaaaaaaa");

// 코드 가독성 더 좋게 줄여보자
function otherSolution(s) {
  const hash={};

  console.log([...s]);
  // spread operator를 이용해서 배열 형식으로
  return [...s].map((v,i)=>{
      let result = hash[v] !== undefined ? i - hash[v] : -1;
      hash[v] = i;
      return result;
  });
}

otherSolution("banana");
