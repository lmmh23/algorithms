
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