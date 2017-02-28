from random import choice

class RandomWalk():
	#生成随机漫步数据
	def __init__(self, num_points=5000):
		#初始化漫步数据的属性
		self.num_points = num_points

		#所有随机漫步都始于（0，0）
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		#计算随机漫步包含的而所有点
		while len(self.x_values) < self.num_points:
			#决定前景方向已经沿着这个方向前进的距离
			x_direction = choice([1, -1])
			x_distance = choice([0,1,2,3,4])
			x_step = x_direction*x_direction

			y_direction = choice([1, -1])
			y_distance = choice([0,1,2, 3, 4])
			y_step = y_distance*y_direction

			#拒绝原地踏步
			if x_step == 0 and y_step == 0:
				continue
			#计算下一个点的x和y值

			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)