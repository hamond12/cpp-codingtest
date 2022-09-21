import collections

n, m = map(int, input().split())  # 세로, 가로

maze = [list(map(int, input().split())) for i in range(n)]

#이동할 네 방향 정의(상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#bfs->시작지점에서 가까운 노드부터 그래프의 모든 노드 차례대로 탐색 
def bfs(x, y):

    #큐 구현을 위해 deque라이브러리 호출
    queue = collections.deque([(x, y)])

    #시작지점의 값은 1
    maze[x][y] = 1 

    #큐가 빌때까지 반복
    while queue: 

        x, y = queue.popleft()

        #현재 위치에서 4방향으로 위치 확인
        for i in range(4): 
            nx, ny = x+dx[i], y+dy[i]

            #미로찾기 공간을 벗어나지 않거나 탐색한 요소의 값이 1일때 
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1 
                queue.append((nx, ny))
                
    #미로의 도착점에 해당하는 값 출력
    return maze[n-1][m-1]

#배열은 0부터 시작-> 미로 시작 위치(1,1) = maze[0][0] 
print(bfs(0, 0))
