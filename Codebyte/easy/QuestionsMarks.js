function QuestionMarks(str) {
  let result = false;
  for (let i = 0; i < str.length; i++) {
    for (let j = i + 1; i < str.length; j++) {
      if (Number(str[i]) + Number(str[j]) === 10) {
        result = true;
        if (str.slice(i, j).split("?").length - 1 < 3) {
          // 하나라도 아니라면 false를 return 해버려야함.
          return false;
        }
      }
    }
  }
  return result;
}
