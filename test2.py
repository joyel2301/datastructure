import turtle, random
import time

def draw_tree(depth, length, angle):
    if depth > 0:
        t.forward(length)
        t.left(angle)
        draw_tree(depth - 1, length * 0.75, angle)  # 왼쪽 가지 뻗기
        t.right(angle + angle)
        draw_tree(depth - 1, length * 0.75, angle)  # 오른쪽 가지 뻗기
        t.left(angle)
        t.backward(length)
    else:
        t.dot(5, random.choice(['red', 'green']))  # 색상 선택 수정

t = turtle.Turtle()
t.setheading(90)  # 초기 진행 방향을 북쪽으로 설정
t.speed(0)  # 가장 빠르게 그리도록 설정

start = time.time()  # 시작할 때 시간을 기록
draw_tree(10, 100, 30)
end = time.time()  # 끝날 때 시간을 기록
print("나무를 그리는데", end - start, "초가 걸렸습니다.")  # 문자열 따옴표 수정