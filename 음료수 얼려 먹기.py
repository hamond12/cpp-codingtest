# 얼음틀의 세로, 가로 길이
n, m = map(int, input().split())

# 아이스박스에 값 추가
ice_box = []
for i in range(n):
    ice_box.append(list(map(int, input().split())))

#구멍이 뚫려있는 부분을 찾으면 True반환하는 함수
def dfs(x, y):

    #x,y값이 아이스박스 크기를 초과하면 False반환
    if -1 >= x or x >= n or -1 >= y or y >= m:
        return False

    #탐색하는 아이스박스의 성분이 0인경우(얼음이 얼 수 있는 곳)
    if ice_box[x][y] == 0:
        ice_box[x][y] = 1  # 해당 성분 방문 표시
        dfs(x - 1, y) #상
        dfs(x + 1, y) #하
        dfs(x, y - 1) #좌
        dfs(x, y + 1) #우
        return True

    #ice_box{x][y]값이 1이면(칸막이로 막혀있으면) False반환
    return False


#함수결과가 True인 개수를 카운트
cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)
