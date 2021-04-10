import random
data = []
count = 0
with open('reviews.txt', 'r') as f:  #with可以自動關閉讀取檔案
	for line in f:
		data.append(line)
		count += 1
		if  count % 100000 == 0:  # 求餘數時使用%
			print(len(data))

print('檔案讀取完ㄌ，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len += len(d)
	#print(sum_len)

print('留言的平均長度為', sum_len/len(data))

s = 1
y = 21741
z = random.randint(s, y)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print(z)
print('一共有', len(new), '筆留言長度小於100')
print('第', z, '筆資料為: ')
print(new[z])