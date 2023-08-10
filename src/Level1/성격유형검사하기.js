

function solution(survey, choices) {
  var answer = '';

  const mbtiMap = {
    R: 0, T: 0,
    C: 0, F: 0,
    J: 0, M: 0,
    A: 0, N: 0
  }

  let score = [3, 2, 1, 0, 1, 2, 3];

  survey.forEach((sur, idx) => {
    if (choices[idx] < 4) {
      mbtiMap[sur[0]] += score[choices[idx] - 1];
    } else if (choices[idx] > 4) {
      mbtiMap[sur[1]] += score[choices[idx] - 1];
    }
  })

  console.log(mbtiMap);

  mbtiMap['R'] >= mbtiMap['T'] ? answer += 'R' : answer += 'T'
  mbtiMap['C'] >= mbtiMap['F'] ? answer += 'C' : answer += 'F'
  mbtiMap['J'] >= mbtiMap['M'] ? answer += 'J' : answer += 'M'
  mbtiMap['A'] >= mbtiMap['N'] ? answer += 'A' : answer += 'N'


  // console.log(answer);


  return answer;
}

// solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]);
// solution(["TR", "RT", "TR"], [7, 1, 3]);
// solution(["RT", "RT", "RT"], [7, 2, 4]);  //"TCJA"
// solution(["RT", "RT", "RT"], [7, 5, 2])
// solution(["AN", "NA", "MJ", "JM", "RT", "TR"], [5, 5, 5, 5, 5, 5])


/* 
  다른 사람 풀이.
*/

function solution2(survey, choices) {
  const MBTI = {};
  const types = ["RT", "CF", "JM", "AN"];

  types.forEach((type) =>
    type.split('').forEach((char) => MBTI[char] = 0)
  )

  choices.forEach((choice, index) => {
    const [disagree, agree] = survey[index];

    MBTI[choice > 4 ? agree : disagree] += Math.abs(choice - 4);
  });

  return types.map(([a, b]) => MBTI[b] > MBTI[a] ? b : a).join("");
}

solution2(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]);