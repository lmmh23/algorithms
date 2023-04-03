function solution(park, routes) {
    var answer = [];
    const col = park.length;
    const row = park[0].length;
    const park2D = Array.from(Array(col), () => new Array(row));
    park.forEach((park, index) => {
        for (var i = 0; i < park.length; i++) {
            if (park[i] === 'S') {
                answer[0] = index;
                answer[1] = i;
            }
            park2D[index][i] = park[i];
        }
    })
    console.log(park2D);
    console.log(answer)
    routes.forEach((route, index) => {
        let direction = route.substr(0, 1);
        let distance = parseInt(route.substr(2, 1));
        let isBlock = false;
        switch (direction) {
            case 'W':
                if (answer[1] - distance < 0) break;
                for (var i = 1; i < distance + 1; i++) {
                    if (park2D[answer[0]][answer[1] - i] === 'X') isBlock = true;
                }
                if(!isBlock) answer[1] -= distance;
                break;
            case 'E':
                if (answer[1] + distance >= row) break;
                for (var i = 1; i < distance + 1; i++) {
                    if (park2D[answer[0]][answer[1] + i] === 'X') isBlock = true;
                }
                if(!isBlock) answer[1] += distance;
                break;
            case 'N':
                if (answer[0] - distance < 0) break;
                for (var i = 1; i < distance + 1; i++) {
                    if (park2D[answer[0] - i][answer[1]] === 'X') isBlock = true;
                }
                if(!isBlock) answer[0] -= distance;
                break;
            case 'S':
                if (answer[0] + distance >= col) break;
                for (var i = 1; i < distance + 1; i++) {
                    if (park2D[answer[0] + i][answer[1]] === 'X') isBlock = true;
                }
                if(!isBlock) answer[0] += distance;
                break;
        }
        console.log(answer);
    })
    console.log(answer);
    return answer;
}

solution(["OSO","OOO","OXO","OOO"], ["E 2","S 3","W 1"])

