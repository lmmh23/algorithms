function FindIntersection(strArr) {
  const firstEl = strArr[0].split(", ");
  const secondEl = strArr[1].split(", ");
  const result = firstEl.filter((x) => secondEl.find((a) => a === x));
  return result.length > 0 ? result.join(",") : "false";
}
