function solution(price, money, count) {
  const map = Array.from({ length: count }, (_, idx) => idx + 1);
  const acc = map.reduce((acc, cur) => acc += cur * price, 0);

  return acc - money < 0 ? 0 : acc - money;
}