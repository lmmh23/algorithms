function solution(X, Y) {
  var answer = '';

  const arrX = new Array(10).fill(0);
  const arrY = new Array(10).fill(0);

  X.split("").forEach(item => arrX[item]++);
  Y.split("").forEach(item => arrY[item]++);

  arrX.forEach((x, i) => {
    if (x && arrY[i]) {
      answer += String(i).repeat(Math.min(arrX[i], arrY[i]));
    }
  });

  if (answer !== "" && +answer === 0) return '0';

  console.log(answer);
  return answer.length ? [...answer].reverse().join('') : "-1";
}

solution("12321", "42531");