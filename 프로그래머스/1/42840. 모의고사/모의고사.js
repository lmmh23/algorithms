function solution(answers) {
  // [1, 2, 3, 4, 5, ....] (5번씩 반복)
  // [2, 1, 2, 3, 2, 4, 2, 5, ...] (8번씩 반복)
  // [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...] (10번씩 반복)

  const studentA = [1, 2, 3, 4, 5];
  const studentB = [2, 1, 2, 3, 2, 4, 2, 5];
  const studentC = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  const score = {
    A: 0,
    B: 0,
    C: 0,
  };
  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === studentA[i % 5]) score.A++;
    if (answers[i] === studentB[i % 8]) score.B++;
    if (answers[i] === studentC[i % 10]) score.C++;
  }

  const maxScore = Math.max(...Object.values(score));
  return Object.keys(score)
    .filter((key) => score[key] === maxScore)
    .map((value) => {
      if (value === "A") return 1;
      if (value === "B") return 2;
      if (value === "C") return 3;
    });
}
