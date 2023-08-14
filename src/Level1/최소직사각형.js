function solution(sizes) {
  const X = [];
  const Y = [];

  sizes.forEach((size, _) => {
    const max = Math.max(size[0], size[1]);
    const min = Math.min(size[0], size[1]);
    X.push(max);
    Y.push(min);
  })

  console.log(Math.max(...X) * Math.max(...Y))

  return Math.max(...X) * Math.max(...Y);
}


solution([[60, 50], [30, 70], [60, 30], [80, 40]]); // result: 4000

// 다른사람 풀이.
function solution2(sizes) {
  // 가로를 더 길게 배치.
  const rotated = sizes.map(([w, h]) => w < h ? [h, w] : [w, h]);

  let maxSize = [0, 0];
  // 구조분해 할당. 
  rotated.forEach(([w, h]) => {
    // 최대 높이, 너비 구하기.
    if (w > maxSize[0]) maxSize[0] = w;
    if (h > maxSize[1]) maxSize[1] = h;
  })
  return maxSize[0] * maxSize[1];
}