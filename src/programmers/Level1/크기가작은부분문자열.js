
const splitNumber = (split, n) => {
  let splited = [];
  while (split.length >= n) {
    splited.push(split.slice(0, n))
    split = split.slice(1);
  }
  return splited;
}

function solution(a, b) {
  var answer = 0;
  const splited = splitNumber(a, b.length);
  let compare;
  if (b < 10) {
    compare = '0' + b.toString();
  } else {
    compare = b.toString();
  }
  splited.forEach((value, _) => value <= b.toString() && answer++);

  console.log(answer);
  return answer;
}


solution("3141592", "271");
solution("500220839878", "7");
solution("10203", "15")


function otherSolution(t, p) {
    let count = 0;
    for(let i=0; i<=t.length-p.length; i++) {
        let value = t.slice(i, i+p.length);
        // js에서 숫자로만 이루어진 문자열 앞에 +를 붙이면 숫자로 변환됨. 개꿀팁
        if(+p >= +value) count++;
    }
    return count;
}