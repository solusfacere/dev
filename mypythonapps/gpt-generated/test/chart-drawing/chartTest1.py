import matplotlib.pyplot as plt

# 체중 변화 및 목표 데이터를 바탕으로 한 차트
current_weight = 73.7
goal_weight = 80

# 데이터 설정
data = {'Current Weight': current_weight, 'Goal Weight': goal_weight}

# 차트 생성
fig, ax = plt.subplots()
ax.bar(data.keys(), data.values(), color=['blue', 'green'])

# 차트 타이틀 및 레이블 설정
ax.set_title('Current Weight vs Goal Weight')
ax.set_ylabel('Weight (kg)')

# 차트 표시
plt.show()
