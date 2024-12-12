function solution(video_len, pos, op_start, op_end, commands) {
  const videoLenS = toSecond(video_len);
  let posS = toSecond(pos);
  const opStartS = toSecond(op_start);
  const opEndS = toSecond(op_end);

  if (posS >= opStartS && posS <= opEndS) posS = opEndS;

  for (let i = 0; i < commands.length; i++) {
    posS += commands[i] === "next" ? 10 : -10;
    if (posS < 0) {
      posS = 0;
    }
    if (posS > videoLenS) {
      posS = videoLenS;
    }
    if (posS >= opStartS && posS <= opEndS) {
      posS = opEndS;
    }
  }

  const h = Math.floor(posS / 60) + "";
  const m = (posS % 60) + "";

  return `${h.padStart(2, "0")}:${m.padStart(2, "0")}`;
}

function toSecond(target) {
  const [minute, second] = target.split(":");
  return Number(minute) * 60 + Number(second);
}

console.log(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"]));
