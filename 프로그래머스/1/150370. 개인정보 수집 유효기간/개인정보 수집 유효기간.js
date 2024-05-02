function solution(today, terms, privacies) {
  var answer = [];
  const map = {};

  for (const term of terms) {
    const splited = term.split(" ");
    map[splited[0]] = parseInt(splited[1]);
  }

  let idx = 1;
  for (const privarcy of privacies) {
    const splited = privarcy.split(" ");
    const parts = splited[0].split(".");

    let year = parseInt(parts[0], 10);
    let month = parseInt(parts[1], 10);
    let day = parseInt(parts[2], 10);

    year += Math.floor((month + map[splited[1]] - 1) / 12);
    month = (month + map[splited[1]] - 1) % 12 + 1;

    if (month < 10) {
      month = '0' + month;
    }
    if (day < 10) {
      day = '0' + day
    }
    const dateString = year + '.' + month + '.' + day;
    
    if (dateString.toString() <= today) {
      answer.push(idx);
    }
    idx++;
  }
  console.log(answer);
  return answer;
}
