friend = ['Korkai','Khorkai','Khorkwai','Somchai','Somsak']

friend2 = {'Korkai':'คุณก.ไก่',
		   'Khorkai':'คุณข.ไข่'}

visitor = 'Somchai'

if visitor in friend or visitor.title() in friend:
	print('เป็นเพื่อนลุงเอง เชิญขึ้นมาได้เลย')
	if visitor in friend2 or visitor.title() in friend2:
		print('สวัสดี' + friend2[visitor.title()])
	else:
		print('สวัสดีคุณลูกค้า')

else:
	print('เฮ้ย! คุณคือใคร ไม่มีชื่อในเมมเบอร์')