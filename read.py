data = []
count = 0
with open('reviews.txt', 'r') as f:  #with可以自動關閉讀取檔案
	for line in f:
		data.append(line)
		count += 1
		if  count % 1000 == 0:  # 求餘數時使用%
			print(len(data))

print(len(data))

print(data[0])
print('-------------------------------------------------')
print(data[1])