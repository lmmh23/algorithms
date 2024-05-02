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