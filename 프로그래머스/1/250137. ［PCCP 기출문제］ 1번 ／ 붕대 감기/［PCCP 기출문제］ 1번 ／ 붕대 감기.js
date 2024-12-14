function solution(bandage, health, attacks) {
  const prepareTime = bandage[0];
  const recoveryPerSecond = bandage[1];
  const additionalRecovery = bandage[2];

  let answer = health;
  for (let i = 0; i < attacks.length; i++) {
    answer -= attacks[i][1];

    if (answer <= 0) return -1;

    if (i !== attacks.length - 1) {
      const time = attacks[i + 1][0] - attacks[i][0] - 1;
      const additional = Math.floor(time / prepareTime);
      answer += time * recoveryPerSecond + additionalRecovery * additional;
      if (answer >= health) answer = health;
    }
  }

  return answer <= 0 ? -1 : answer;
}
