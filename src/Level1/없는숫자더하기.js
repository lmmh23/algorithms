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

solution([1, 2, 3, 4, 6, 7, 8, 0]);
solution([5, 8, 4, 0, 6, 7, 9]);


function solution2(numbers) {
  return 45 - numbers.reduce((cur, acc) => cur + acc, 0);
}