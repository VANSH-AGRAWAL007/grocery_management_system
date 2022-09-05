from tkinter import font
import biller
import item_adder
from tkinter import *
from closenotebook import *
import calculator
import csv

class home(Tk):
	frames = []
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.state('zoomed')
		# print(super())

		menubar = Menu(self)
		filemenu = Menu(menubar,tearoff =0)
		windowmenu = Menu(menubar,tearoff= 0)

		windowmenu.add_command(label='calculator',command=biller.calc)

		filemenu.add_command(label = "Open Bill",command=self.open_bill)
		filemenu.add_command(label = "Add Customer",command = biller.ob_adder)
		filemenu.add_command(label='EXIT',command=quit)

		windowmenu.add_command(label = "Biller",command = lambda: self.add_billing())
		windowmenu.add_command(label = "New Item Adder",command = lambda: self.add_item_adder())
		windowmenu.add_command(label = "Stock Adder",command = lambda: self.stock_item_adder())

		# datamenu.add_command(label = "Export Data",command = biller.ob_adder)
		# datamenu.add_command(label = "P&L Report",command = biller.ob_adder)



		menubar.add_cascade(label = 'file',menu=filemenu )
		menubar.add_cascade(label = 'window',menu=windowmenu)

		Tk.config(self,menu= menubar)

		ribbon = Frame(self,relief=RIDGE,borderwidth = 1)
		
		self.container = CustomNotebook(self,width=1000, height=500)


		ribbon.pack(side= 'top',anchor='w',fill=X)
		self.container.pack(side = 'top',fill =BOTH,anchor='w',padx=45,expand=True)
		
		# f = Frame(self.container, background="red")
		# self.container.add(f, text='red')

		# container.grid_columnconfigure(0,weight=1)
		# container.grid_rowconfigure(0,weight=1)

		ribonmenu = Ribbon(ribbon,self)

		# self.frames[biller.bill] = frame

		# frame.grid(row=1,column=0,sticky='e')
		ribonmenu.grid(row=0,column=0,sticky='w')

		# self.showframe(biller.bill)
		# self.showframe(StartPage)

	def forgetcurrent(self):
		for item in self.container.winfo_children():
			if str(item)==self.container.select():
				item.destroy()       
				return
	
	def forgetstockadder(self):
		for item in self.container.winfo_children():
			# print(type(item.winfo_children()[0]))
			if type(item.winfo_children()[0]) == item_adder.stock_up_frame:
				item.destroy()       
				return
		

	def showframe(self,contain):
		frame = self.frames[contain]
		frame.tkraise()

	def add_billing(self):
		# print(self.container," container")
		billparent = Frame(self.container)
		a=biller.bill(billparent,self)
		# print(self," self")
		a.pack(anchor = W, expand = True,fill = Y)
		self.container.add(billparent,text = 'BILLER')

	def add_item_adder(self):
		itemadderparent = Frame(self.container)
		a = item_adder.item_adder(itemadderparent)
		a.pack(anchor= W)
		self.container.add(itemadderparent,text="ITEM ADDER")
	
	def stock_item_adder(self):
		stockadderparent = Frame(self.container)
		a = item_adder.stock_up_frame(stockadderparent)
		a.pack(anchor= W)
		self.container.add(stockadderparent,text="STOCK ADDER")
	
	def open_bill(self):
		def selection():
			sel = lb.curselection()
			billnum = billdata[sel[0]][0]
			# print(billnum)
			self.open_bill_acc(billnum)

		openbillselector = Toplevel(self)
		lb= Listbox(openbillselector,selectmode=SINGLE,width = 30)
		lb.pack()
		
		but = Button(openbillselector,text = "OPEN",command = selection)
		but.pack()
		
		with open('Data_files\\bill_list.csv',newline='\n') as f:
			alldata = csv.reader(f,delimiter = ',')
			billdata,j={},0
			for i in alldata:
				billdata[j] = i
				j+=1
			print(billdata)
			for i in range(len(billdata)):
				j=billdata[i]
				lb.insert(i,"{0} : {1}".format(j[0],j[1]))
		

		openbillselector.mainloop()

	def open_bill_acc(self,billnum):
		with open('bill\\bill{0}.txt'.format(billnum),'r') as f:
			selbilldata = f.readlines()
		it_data = ['','','']
		for i in range(4,len(selbilldata)):
			selline = selbilldata[i].split(':')
			# print(selline)
			if selline[1]:
				it_data[0] = it_data[0]+selline[0]+'\n'
				it_data[1] = it_data[1]+selline[1]+'\n'
				it_data[2] = it_data[2]+selline[2]
			# print(it_data)
		opened = biller.Bill(selbilldata[2],selbilldata[3],it_data,self,False)


class Ribbon(Frame):
	def __init__(self,parent,master):
		Frame.__init__(self,parent)

		self.master =master

		HOME_IMG_CALC=PhotoImage(file="Resources\\calculator(2).png")
		HOME_IMG_DATA=PhotoImage(file="Resources\\database(large)1.png")
		HOME_IMG_ADD=PhotoImage(file="Resources\\friend(large).png")
		HOME_IMG_BILL=PhotoImage(file="Resources\\money.png")

		self.database_button=Button(self,image=HOME_IMG_DATA,borderwidth=0,background="light yellow",command= self.master.stock_item_adder)
		self.database_button.image= HOME_IMG_DATA

		self.add_button= Button(self,image=HOME_IMG_ADD,border=0,background="light yellow",command =lambda: biller.ob_adder(None))
		self.add_button.image= HOME_IMG_ADD

		self.calculate= Button(self,image=HOME_IMG_CALC,border=0,background="light yellow",command = calculator.calculator) 
		self.calculate.image= HOME_IMG_CALC

		self.bill_button=Button(self,image=HOME_IMG_BILL,border=0,background="light yellow",command= self.master.add_billing)
		self.bill_button.image= HOME_IMG_BILL


		self.database_button.grid(row=1,column=1,padx=50,pady=10,sticky="e")
		self.calculate.grid(row=1,column=3)
		self.add_button.grid(row=1,column=4,padx=50,sticky="e")
		self.bill_button.grid(row=1,column=5,padx=50,sticky="e")

			
	
