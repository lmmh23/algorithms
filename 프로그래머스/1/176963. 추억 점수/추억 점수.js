function solution(name, yearning, photo) {


  var answer = [];

  for (let i = 0; i < photo.length; i++) {
    let result = 0;
    for (let j = 0; j < name.length; j++) {
      if (photo[i].includes(name[j])) {
        result += yearning[j];
      }
    }
    answer.push(result);
  }

  console.log(answer);
  return answer;
};

solution(
  ["kali", "mari", "don"],
  [11, 1, 55]	,
  [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
);