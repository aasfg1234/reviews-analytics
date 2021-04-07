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