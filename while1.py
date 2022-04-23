# while1.py

money = 1000
transfer = 10000

print('Check:', money < transfer)

while money < transfer:
	print('กรุณากรอกตัวเลขโอนใหม่ค่ะ')
	transfer = int(input('new transfer: '))
	if transfer > 1000000:
		print('เรียกผู้จัดการมา ขอเคลียร์ก่อนถึงจะโอนได้')
		break

print('โอนได้ถ้าผู้จัดการอนุญาตสำหรับกรณีเป็น VIP')