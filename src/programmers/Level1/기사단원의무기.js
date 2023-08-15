function countDivisors(number) {
  let count = 0;

  for (let i = 1; i * i <= number; i++) {
    if (i * i === number) count++;
    else if (number % i == 0) count +=2
  }

  return count;
}

function solution(number, limit, power) {
  var answer = 0;

  const array = Array.from({ length: number }, (_, idx) => idx + 1);
  
  for (const n of array) {
    const measure = countDivisors(n);
    if (measure > limit) {
      answer += power;
    } else {
      answer += measure;
    }
  }
  console.log(answer);
  return answer;
}

solution(5, 3, 2);
solution(10, 3, 2);