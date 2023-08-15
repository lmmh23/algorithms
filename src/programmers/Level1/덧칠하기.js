function solution(n, m, section) {
  let answer = 0;

  let painted = 0;
  section.forEach((n) => {
    // console.log("PAINTED", painted);
    if (n > painted) {
      painted = n + m - 1;
      answer++;
    }
  });
  // console.log(answer);
  return answer;
}
solution(8, 4, [2, 3, 6]);  // 2
solution(5, 4, [1, 3]);     // 1
solution(4, 1, [1, 2, 3, 4]); // 4

function otherSolution(n, m, section) {
  let count = 0;
  const arr = Array.from(Array(n + 1).fill(null));

  section.forEach(el => {
    arr[el] = 1;
  })

  section.forEach(el => {
    if (arr[el]) {
      arr.fill(null, el, el + m)
      count++
    }
  })
  return count
}

otherSolution(8, 4, [2, 3, 6]);  // 2
otherSolution(5, 4, [1, 3]);     // 1
otherSolution(4, 1, [1, 2, 3, 4]); // 4