function solution(numbers) {
  var answer = 0;

  let temp = false;

  const check = Array.from({ length: 10 }, (_, index) => index);
  check.forEach((num, _) => {
    if (!numbers.includes(num)) {
      temp = true;
      answer += num;
    }
  })

  // console.log(answer);

  if (!temp) return -1;
  else return answer;

}