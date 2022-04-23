# forloop1.py

# ลูปตามจำนวน
for i in range(5):
	print('Hello',i)

print('----Loop in List----')
friend = ['Korkai','Khorkai','Khorkwai','Somchai','Somsak']

for f in friend:
	print(f)
	if f == 'Korkai':
		print('สวัสดีคุณก.ไก่')
	else:
		print('สวัสดีคุณลูกค้า')
print('----Loop in Dictionary----')

friend2 = {'Korkai':'คุณก.ไก่',
		   'Khorkai':'คุณข.ไข่',
		   'Somchai':'คุณสมชาย'}

# show key
for f in friend2:
	print(f)

# show items
for k,v in friend2.items():
	print('Key:',k)
	print('Value:',v)

# show key only
for f in friend2.keys():
	print(f)

# show value only
for f in friend2.values():
	print(f)

# ต้องการลำดับ
for i,f in enumerate(friend,start=1000):
	print(i,f)

# ต้องการลำดับสำหรับ dict
for i,f in enumerate(friend2.items()):
	print(i,f)

# ต้องการลำดับสำหรับ dict แยก key
for i,(k,v) in enumerate(friend2.items()):
	print(i,k,v)