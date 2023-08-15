function solution(number) {
  
  // number = [-2, 3, 0, 2, -5]
  // 결과를 저장할 변수
  let result = 0;
  const combination = (current, start) => {
    console.log(current);
    if (current.length === 3) {
      result += current.reduce((acc, cur) => acc + cur, 0) === 0 ? 1 : 0;
      return;
    }
    for (let i = start; i < number.length; i++) {
      combination([...current, number[i]], i + 1);
    }
  }

  combination([], 0);

  return result;

}

solution([-2, 3, 0, 2, -5]);