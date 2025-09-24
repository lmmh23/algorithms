def solution(friends, gifts):
  friendsLength = len(friends)
  # 친구 이름 -> 인덱스
  nameToIdx = {name: i for i, name in enumerate(friends)}
  # 선물 기록 giftCount[giver][receiver]
  giftCount = [[0] * friendsLength for _ in range(friendsLength)]

  # 기록 누적
  for gift in gifts:
    giver, receiver = gift.split(" ")
    giverIdx, receiverIdx = nameToIdx[giver], nameToIdx[receiver]
    giftCount[giverIdx][receiverIdx] += 1

  totalGiven = [sum(giftCount[i]) for i in range(friendsLength)]
  totalReceived = [sum(giftCount[j][i] for j in range(friendsLength)) for i in range(friendsLength)]
  giftScore = [totalGiven[i] - totalReceived[i] for i in range(friendsLength)]

  nextReceive = [0] * friendsLength
  for i in range(friendsLength):
    for j in range(i+1, friendsLength):
      if giftCount[i][j] > giftCount[j][i]:
        # i가 j에게서 1개 받음
        nextReceive[i] += 1
      elif giftCount[i][j] < giftCount[j][i]:
        # j가 i에게서 1개 받음
        nextReceive[j] += 1
      else:
        # 동일하면 선물 지수 비교
        if giftScore[i] > giftScore[j]:
          nextReceive[i] += 1
        elif giftScore[i] < giftScore[j]:
          nextReceive[j] += 1
        # 같으면 변화 없음

  return max(nextReceive) if nextReceive else 0