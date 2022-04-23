# GUI-calculator.py

from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk() #ทีตัวใหญ่ เคตัวเล็ก
GUI.title('โปรแกรมคำนวณราคาปลา รถพุ่มพวงของลุง')
GUI.geometry('700x600')

bg = PhotoImage(file='car.png')
# bg = PhotoImage(file= r'C:\Users\Uncle Engineer\Desktop\Basic Python\car.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='กรุณากรอกจำนวนปลา (กิโลกรัม)',font=(None,20))
L.pack()

v_quantity = StringVar() # เป็นตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack()

def Cal():
	try:
		quan = float(v_quantity.get())
		calc = quan * 39 # 39 บาทต่อกิโล * จำนวนปลาที่กรอกมา
		messagebox.showinfo('ราคาทั้งหมด','ราคาปลาทั้งหมด {} บาท'.format(calc) )
		v_quantity.set('')
		E1.focus()
	except:
		messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
		v_quantity.set('1')
		E1.focus()

B = ttk.Button(GUI, text='คำนวณ',command=Cal)
B.pack(ipadx=30,ipady=20,pady=20) #ipadx ขยายความกว้าง x/y

GUI.mainloop() # เพื่อให้โปรแกรมรันตลอดเวลา