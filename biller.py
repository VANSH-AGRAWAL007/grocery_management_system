from tkinter import *
import csv
from tkinter.ttk import Combobox
from tkinter import messagebox
from datetime import date
import matplotlib.pyplot as pl
from datetime import date
# import sys
# sys.path.insert(1,'/Resouces')
# from Resources import home



today =str(date.today())
font_set =  'Hobostd {0:d}'

customer_dat = {}
item_dat = {}
def itemdata_reader():
	with open('Data_files\\item_file.csv',newline = '\n') as it:
		alldata = csv.reader(it,delimiter = ',')		
		for i in alldata:
			if i != []:
				item_dat[i[0]] = [i[3],i[1],i[2],i[4]]
	return item_dat

# item_dat = itemdata_reader()
# print(item_dat)


# it_dat = list(item_dat.keys())
# it_dat.sort()

def custfresher():
	global customer_dat
	with open('Data_files\\customer_file.csv',newline='\n') as cust:
		alldata = csv.reader(cust,delimiter=',')
		for i in alldata:
			customer_dat[i[0]] = i[1]
	return custfresher
custfresher()
# print(customer_dat)
ent_dat= list(customer_dat.keys())
ent_dat.sort()

def update_itemfile():
	writedata=[]
	for i in item_dat:
		writedata.append([i,item_dat[i][1],item_dat[i][2],item_dat[i][0],item_dat[i][3]])
	writedata.pop()
	# print(writedata)
	with open('Data_files\\item_file.csv','r+',newline = '\n') as it:
		writer= csv.writer(it,delimiter = ',')
		for i in writedata:
			writer.writerow(i)

def addnow(x,y,self):
	# print('hello')
	with open('Data_files\\customer_file.csv',mode='a',newline='\n') as cust:
		alldata = csv.writer(cust,delimiter=',')
		alldata.writerow([str(x),y])
	ob_adder_window.destroy()
	custfresher()
	ent_dat= list(customer_dat.keys())
	ent_dat.sort()
	# print(self)
	if self:
		# print(self)
		self.ent_name['values']=ent_dat
	return ent_dat
	# print(ent_dat)
	

def ob_adder(self):
	global ob_adder_window
	ob_adder_window = Tk()
	ob_adder_window.geometry('300x180')
	ob_adder_window.title('CUSTOMER ADDING..')
	ob_adder_window.configure(background= 'ivory')


	obj_type= 'customer name : '.capitalize()
	sec_type = 'phone no. : '.capitalize()
	obj_lab = Label(ob_adder_window,text = obj_type,background= 'ivory')
	sec_lab = Label(ob_adder_window,text = sec_type,background= 'ivory')
	obj_ent = Entry(ob_adder_window,text ='',width=25)
	sec_ent = Entry(ob_adder_window,text ='',width=25)
	submit = Button(ob_adder_window,border= 5,text= "ADD",command = lambda : addnow(obj_ent.get(),sec_ent.get(),self),background= 'ivory')

	obj_lab.pack()
	obj_ent.pack(fill = X,padx= 20) 
	sec_lab.pack()
	sec_ent.pack(fill = X,padx= 20)
	submit.pack(anchor = S,fill = X,pady= 20,padx= 20)
	ob_adder_window.mainloop()
	# print("hi")

	

def calc():
	import calculator



class bill(Frame):

	
	def __init__(self, parent,master):
		super().__init__(parent)
		item_dat = itemdata_reader()
		it_dat = list(item_dat.keys())
		it_dat.sort()

		self.master = master
		# print(master)

		self.config(width = 1000,height=700)

		self.add_tocartimg= PhotoImage(file="Resources\\add_to_cart.png")
		self.entrimg= PhotoImage(file='Resources\\entr.png')
		# self.calcimg = PhotoImage(file='Resources\\calculator.png')
		# self.dataimg = PhotoImage(file='Resources\\database.png')
		# self.graphimg = PhotoImage(file='Resources\\graph.png')

		self.labItemAdded= ['','','']

		self.lab_name = Label(self,text= 'Name Of Customer:>'.upper(),font = font_set.format(15))
		self.ent_name = Combobox(self,width= 50,values=ent_dat,font= font_set.format(15))
		self.lab_cont = Label(self,text = 'select item:>'.upper(),width = 30,font=font_set.format(15))
		self.it_ent_name = Combobox(self,text =None,width = 50,font=font_set.format(15),values= it_dat)
		self.entr = Button(self,image=self.entrimg,command = self.cum,fg='white',border =0)
		self.lab_it_cnt = Label(self,text='select Quantity:> '.upper(),font=font_set.format(10))
		self.it_spin_cnt = Spinbox(self,from_ = 1,to = 10,font=font_set.format(10),width=20)
		self.but_it_add= Button(self,image = self.add_tocartimg,command =lambda: self.additem(self.labItemAdded) if (self.it_ent_name.get()) else lambda: 10,border=0).grid(row= 3,column=1,sticky='e',columnspan=2)
		self.labfrm_itname = LabelFrame(self,text ='ITEMS',relief=SUNKEN)
		self.lab_itemadded= Label(self.labfrm_itname,text=self.labItemAdded[0],font=font_set.format(10),width = 50,height = 20)
		self.labfrm_itcnt= LabelFrame(self,text ='COUNT',relief= SUNKEN)
		self.lab_itemaddedcnt = Label(self.labfrm_itcnt,text=self.labItemAdded[1],font=font_set.format(10),width = 40,height = 20)
		self.labfrm_itcost = LabelFrame(self,text ='COST',relief= SUNKEN)
		self.lab_itemaddedcost= Label(self.labfrm_itcost,text=self.labItemAdded[2],font=font_set.format(10),width = 40,height = 20)
		# self.but_calc = Button(self,image =self.calcimg,border =0 ,background = 'ivory',command=calc).grid(row=6,column=0,sticky='n')
		# self.but_data= Button(self,image =self.dataimg,border =0 ,background = 'ivory',command=datacaller ).grid(row=6,column=1,sticky='n')
		# self.but_graph= Button(self,image =self.graphimg,border =0 ,background = 'ivory',command=graphcaller ).grid(row=6,column=2,sticky='n')
	

		self.lab_name.grid(row=0,column=0,sticky='w',pady= 2)
		self.ent_name.grid(row=0,column=1,columnspan=2,sticky='e')
		self.lab_cont.grid(row=1,column=0,sticky = 'w',pady=2)
		self.it_ent_name.grid(row=1,column=1,columnspan=2,sticky='e')
		self.lab_it_cnt.grid(row=2,column=0,sticky='s',pady= 2)
		self.it_spin_cnt.grid(row=2,column= 2,sticky='s')
		self.labfrm_itname.grid(row=4,column=0,sticky='s')
		self.lab_itemadded.pack(fill=Y,expand= True,anchor='n')
		self.labfrm_itcnt.grid(row =4,column= 1,sticky='s')
		self.lab_itemaddedcnt.pack()

		self.labfrm_itcost.grid(row =4,column= 2,sticky='n')
		self.lab_itemaddedcost.pack()

		self.entr.grid(row=5,column=2,sticky ='n')

	def additem(self,labItemAdded):
		item_dat = itemdata_reader()
		# print(item_dat)
		if self.it_spin_cnt.get():
			# print()
			if int(item_dat[self.it_ent_name.get()][1])-int(self.it_spin_cnt.get())>=0:
				self.labItemAdded[0] += self.it_ent_name.get()+'\n'
				self.labItemAdded[1] += str(self.it_spin_cnt.get()) +'\n'
				self.labItemAdded[2] += str(int(self.it_spin_cnt.get())*int(item_dat[self.it_ent_name.get()][0]))+'\n'
				item_dat[self.it_ent_name.get()][1]=str(int(item_dat[self.it_ent_name.get()][1])-int(self.it_spin_cnt.get()))

			else:
				messenger = messagebox.showwarning('NOT ENOUGH STOCK','NOT ENOUGH STOCK')
				# import view_database
		else:
			self.labItemAdded[1] +='1'+'\n'
			self.labItemAdded[2] += str(1*int(item_dat[self.it_ent_name.get()][0]))+'\n'
		
		# print(int(item_dat[self.it_ent_name.get()][0]))
		self.lab_itemadded.configure(text=self.labItemAdded[0])
		self.lab_itemaddedcnt.configure(text=self.labItemAdded[1])
		self.lab_itemaddedcost.configure(text=self.labItemAdded[2])

		
	def cum(self):

		if self.ent_name.get() not in customer_dat:
			messenger = messagebox.askquestion('new customer found','Add new name??')
			# print(messenger)
			if messenger == 'yes':
				ob_adder(self)
				# print("hi")
				# print(ent_dat)
				self.ent_name.configure(values = ent_dat)
				# print(ent_dat)
			else:
				self.ent_name.set('')
		else:
			total=' '
			it_name=self.labItemAdded[0].split('\n')
			it_cnt= self.labItemAdded[1].split('\n')
			it_cost = self.labItemAdded[2].split('\n')
			it_cost = [int(it_cost[i]) for i in range(len(it_cost)-1)] 
			it_cnt = [int(it_cnt[i]) for i in range(len(it_cnt)-1)]
			it_name = [str(it_name[i]) for i in range(len(it_name)-1)]
			# for i in range(len(it_name)):
			# 	item_dat[it_name[i]][1] = int(item_dat[it_name[i]][1]) - int(it_cnt[i])
			# print(item_dat,"hi")
			update_itemfile()
			# print(self.ent_name.get())
			bill = Bill(self.ent_name.get(),customer_dat[self.ent_name.get()],self.labItemAdded,self.master,True)

	



class Bill(Tk):
	def __init__(self,cust_name,cust_phone,it_data,master,new):
		Tk.__init__(self)
		self.master = master
		# print(master," master")
		today =str(date.today())
		font_set = 'Hobostd {0:d}'

		total=' '
		self.cust_name = cust_name
		self.cust_phone = cust_phone
		self.it_name=it_data[0].split('\n')
		self.it_cnt= it_data[1].split('\n')
		self.it_cost = it_data[2].split('\n')


		self.it_cost = [int(self.it_cost[i]) for i in range(len(self.it_cost)-1)] 
		self.it_cnt = [int(self.it_cnt[i]) for i in range(len(self.it_cnt)-1)]
		self.it_name = [str(self.it_name[i]) for i in range(len(self.it_name)-1)]
		self.totalcos = sum(self.it_cost)
		self.totalcnt= sum(self.it_cnt)
		
		self.geometry('300x400')

	# global saveimg
	# saveimg = PhotoImage(file='print_save.png')
	

		self.lab_name= Label(self,text= 'customer name : {0:s}'.format(cust_name).capitalize(),font =font_set.format(13))
		self.lab_phone = Label(self,text= 'customer phone : {0:d}'.format(int(cust_phone)).capitalize(),font =font_set.format(13))
		self.labfrm_it_n = LabelFrame(self,text= 'ITEMS')
		self.lab_itname = Label(self.labfrm_it_n,text = it_data[0],font =font_set.format(13))
		self.labfrm_it_cnt = LabelFrame(self,text= 'QUANTITY')
		self.lab_itcnt = Label(self.labfrm_it_cnt,text = it_data[1],font =font_set.format(13))
		self.labfrm_it_cost = LabelFrame(self,text= 'COST')
		self.lab_itcost = Label(self.labfrm_it_cost,text = it_data[2],font =font_set.format(13))
		self.labfrm_total= LabelFrame(self,text= 'TOTAL')
		self.lab_totalcnt = Label(self.labfrm_total,text = str(self.totalcnt),font =font_set.format(13))
		self.lab_totalcost =Label(self.labfrm_total,text = str(self.totalcos),font =font_set.format(13))
		self.but_save = Button(self,text='SAVE' if new else 'DONE',command = self.des if new else self.closeBill,border=0,background='ivory',font= font_set.format(13))


		self.lab_name.grid(row=0,column=0,columnspan =2,sticky='w')
		self.lab_phone.grid(row=1,column=0,columnspan =2,sticky='w')
		self.labfrm_it_n.grid(row=2,column=0)
		self.lab_itname.pack(pady=50)
		self.labfrm_it_cnt.grid(row=2,column=1)
		self.lab_itcnt.pack(pady=50)
		self.labfrm_it_cost.grid(row=2,column=2)
		self.lab_itcost.pack(pady=50)
		self.labfrm_total.grid(row=3,column=1,columnspan=2)
		self.lab_totalcnt.grid(row= 0,column=0,padx= 41)
		self.lab_totalcost.grid(row= 0,column=1,pady=10)
		self.but_save.grid(row=4,column=0,columnspan=4)

	def closeBill(self):
		self.destroy()
	def des(self):
		self.salesupdater(self.totalcos)
		self.bill_save()
		self.master.forgetcurrent()
		self.master.add_billing()
		self.master.forgetstockadder()
		self.master.stock_item_adder()
		self.destroy()
	
	def salesupdater(self,tot):
		global sales
		sales = {}
		with open('Data_files\\sales.csv','r+',newline='\n') as sale:
			alldata = csv.reader(sale,delimiter=',')
			for i in alldata:
				sales[i[0]] = i[1]
			# print(sales)
			try:
				sales[today] = str(int(sales[today])+tot)
			except:
				sales[today] = str(tot)
			salesaver = []
			for i in sales:
				salesaver.append([i,sales[i]])
		with open('Data_files\\sales.csv','w',newline = '\n') as sale:
			writer = csv.writer(sale,delimiter = ',')
			for i in salesaver:
				writer.writerow(i)

	def bill_save(self):
		lastbill = []
		with open('Data_files\\bill_list.csv',newline= '\n') as f:
			alldata = csv.reader(f,delimiter = ',')
			for i in alldata:
				if i != []:
					lastbill = i
			if not lastbill:
				lastbill.append(0)
			nextbillno = int(lastbill[0])+1
		with open('Data_files\\bill_list.csv',mode='a',newline= '\n') as f:
			# print(self.cust_name,"     ,<<<-dekho yeh<<<-")
			data = [str(nextbillno),self.cust_name]
			writer= csv.writer(f,delimiter = ',')
			writer.writerow(data)
		with open('bill\\bill{0}.txt'.format(nextbillno),'w') as f:
			f.write('{0}\n'.format(nextbillno))
			f.write(today)
			f.write('\n')
			f.write(self.cust_name)
			f.write('\n')
			f.write(self.cust_phone)
			f.write('\n')
			for i in range(len(self.it_name)):
				name = self.it_name[i]
				quant = self.it_cnt[i]
				cost = self.it_cost[i]
				f.write('{0}:{1}:{2}\n'.format(name,quant,cost))
			

		# 	data = self.cust_name = cust_name
		# self.it_name=it_data[0].split('\n')
		# self.it_cnt= it_data[1].split('\n')
		# self.it_cost = it_data[2].split('\n')
		

