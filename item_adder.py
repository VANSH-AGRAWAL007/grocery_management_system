from tkinter import *
import csv
import biller
# from tkinter.ttk import Combobox
# from tkinter import messagebox

l=["","","","","",""]

class database(Frame):
	def __init__(self,parent):
		super().__init__(parent)
		mainfrm = Frame(self)
		mainfrm.configure(bg = "yellow",width=900)
		mainfrm.pack()
		with open("Data_files\\item_file.csv","r") as f:
			r=csv.reader(f)
			Headings=["item","stock","cost price","selling price","whole seller"]
			item=[]

			for i in r:
				if i != []:
					item.append(i[0]) 
		sb= Scrollbar(mainfrm)
		sb.pack(side =RIGHT,fill=Y)
		frm = Canvas(mainfrm,height=500,width=750, yscrollcommand = sb.set ,scrollregion=(0,0,2000,1000))
		sb.config( command = frm.yview )

		frm.pack(side=LEFT)

		tfrm = Frame(mainfrm)

		canwin = frm.create_window(0,0,window=tfrm,anchor ='nw')

		with open("Data_files\\item_file.csv","r") as file:
			ro=csv.reader(file,delimiter=',')
			a = {}
			for i in ro:
				if i != []:
					g=i[0]
					a[str(g)]=i     

		for i in range(1,6):
			l=Label(tfrm,text=Headings[i-1],bg="khaki",fg="black",padx=20,pady=10,font=("Comic Sans MS",15))
			l.grid(row=0,column=i-1,sticky="snew",padx=4,pady=5)
			tfrm.grid_columnconfigure(i-1,weight=10)   

		self.row_count=a.keys()
		max=len(self.row_count)
		self.quantities = []
		for rows in range(1,max+1): 
			for columns in range(1,6):
				d=item[rows-1]
				s=a[d]
				if rows %2==0:
					color="darkturquoise"
				else:
					color="turquoise"    
				l=Label(tfrm,text= s[columns-1],bg=color,fg="black",padx=20,pady=10,font=("Comic Sans MS",10),takefocus=0)
				if columns == 2:
					self.quantities.append(l)
				l.grid(row=rows,column=columns-1,sticky="snew",padx=4)
				tfrm.grid_columnconfigure(columns-1,weight=10)
		
		sb.config( command = frm.yview )

	def update(self):
		with open("Data_files\\item_file.csv","r") as f:
			r=csv.reader(f)
			Headings=["item","stock","cost price","selling price","whole seller"]
			item=[]

			for i in r:
				if i != []:
					item.append(i) 
		for i,j in enumerate(self.quantities):
			j.configure(text = item[i][1])



class update(Frame):
	def __init__(self,parent):
		super().__init__(parent)
		# update= PhotoImage(file="direct-download.png")
		self.obj_lab = Label(self,text = 'new_item',font=("Comic Sans MS",13))
		self.stock_label = Label(self,text = 'new_amount',font=("Comic Sans MS",13))
		self.obj_ent = Entry(self,text ='',width=25)
		self.stock_ent = Entry(self,text ='',width=25)
		# self.submit = Button(self,image=update,border=0,width = 10)
		self.obj_lab.pack()
		self.obj_ent.pack(fill = X,padx= 20)
		self.stock_label.pack()
		self.stock_ent.pack(fill = X,padx= 20)
		# self.submit.pack(anchor = S,fill = X,pady= 20,padx= 20)
	
	def add(self):
		a={}
		with open("Data_files\\item_file.csv","r") as f:
			r=csv.reader(f)
			item=[]
			copy=[]
			for i in r:
				if i != []:
					copy.append(i)
					item.append(i[0]) 
					a[i[0]]= i[1]
		
		if self.obj_ent.get() in item:
			index = item.index(self.obj_ent.get())
			copy[index][1] = self.stock_ent.get()
			with open("Data_files\\item_file.csv","w",newline='\n') as edit_file:
				write=csv.writer(edit_file)
				for i in range(len(copy)):
					write.writerow(copy[i])



class stock_up_frame(Frame):
	def __init__(self,parent):
		super().__init__(parent)
		self.datawin = database(self)
		self.adderwin = update(self)
		self.addbtn = Button(self,text = 'UPDATE',command = self.add)
		self.datawin.grid(row= 0,column=1,rowspan=2)
		self.adderwin.grid(row=0,column=0)
		self.addbtn.grid(row=1,column = 0)
	
	def add(self):
		self.adderwin.add()
		self.datawin.update()
		# self.datawin.destroy()
		# self.datawin = database(self)
		# self.datawin.grid(row= 0,column=1,rowspan=100)




class item_adder(Frame):
	def __init__(self,parent):
		super().__init__(parent)
		self.configure(background= 'ivory')
# entrimg = PhotoImage(file='entr.png')
		self.label=Label(self,text="ADDING NEW ITEM",font=("Baskerville Old Face",30),background= 'ivory')

		self.item=Entry(self,width=20)
		self.stock=Entry(self,width=20)
		self.cp=Entry(self,width=20)
		self.sp=Entry(self,width=20)
		self.wholeseller=Entry(self,width=20)
	
	
		self.label_item=Label(self,text="item:>",padx=7,pady=5,font=("Comic Sans MS",12),background= 'ivory')
		self.label_stock=Label(self,text="stock:>",padx=7,pady=5,font=("Comic Sans MS",12),background= 'ivory')
		self.label_cp=Label(self,text="cost price:>",padx=7,pady=5,font=("Comic Sans MS",12),background= 'ivory')
		self.label_sp=Label(self,text="selling price:>",padx=7,pady=5,font=("Comic Sans MS",12),background= 'ivory')
		self.label_seller=Label(self,text="whole sellar:>",padx=7,pady=5,font=("Comic Sans MS",12),background= 'ivory')
		self.display_it=LabelFrame(self,text="Items Added",relief= SUNKEN,pady=10,background= 'ivory')
		self.display_st=LabelFrame(self,text="Stocks",relief= SUNKEN,pady=10,background= 'ivory')
		self.display_sp=LabelFrame(self,text="Selling price",relief= SUNKEN,pady=10,background= 'ivory')
		self.display_selle_r=LabelFrame(self,text="Wohesellar",relief= SUNKEN,pady=10,background= 'ivory')
		self.display_cp=LabelFrame(self,text="Celling price",relief= SUNKEN,pady=10,background= 'ivory')
		self.add_item_button = Button(self,padx=7,pady=5,command=self.add_in_data,text ="ADD",border=0)
			
		self.lab_item=Label(self.display_it,text= l[0],bg="ivory")
			
		self.lab_stock=Label(self.display_st,text= l[1],bg="ivory")

		self.lab_sp=Label(self.display_sp,text= l[2],bg="ivory")

		self.lab_cp=Label(self.display_cp,text= l[3],bg="ivory")

		self.lab_seller=Label(self.display_selle_r,text= l[4],bg="ivory")

		self.label.grid(row=0,column=0,columnspan=5)
		self.label_item.grid(row=1,column=0,sticky="W")
		self.item.grid(row=1,column=1,sticky="E",columnspan=4)
		self.label_stock.grid(row=2,column=0,sticky="W")
		self.stock.grid(row=2,column=1,sticky="E",columnspan=4)
		self.label_sp.grid(row=3,column=0,sticky="W")
		self.sp.grid(row=3,column=1,sticky="E",columnspan=4)
		self.label_cp.grid(row=4,column=0,sticky="W")
		self.cp.grid(row=4,column=1,sticky="E",columnspan=4)
		self.label_seller.grid(row=5,column=0,sticky="W")
		self.wholeseller.grid(row=5,column=1,sticky="E",columnspan=4)
		self.add_item_button.grid(row=6,column=1,columnspan=5,sticky="E")

		self.display_it.grid(row=7,column=0,sticky="W")
		self.display_st.grid(row=7,column=1,sticky="W")
		self.display_sp.grid(row=7,column=2,sticky="W")
		self.display_cp.grid(row=7,column=3,sticky="W")
		self.display_selle_r.grid(row=7,column=4,sticky="W")
		self.lab_item.pack(fill=Y)
		self.lab_stock.pack(fill=Y)
		self.lab_sp.pack(fill=Y)
		self.lab_cp.pack(fill=Y)
		self.lab_seller.pack(fill=Y)		
	
	def add_in_data(self):
		with open("Data_files\\item_file.csv","a",newline="\n") as f :
			data=[self.item.get(),str(self.stock.get()),str(self.cp.get()),str(self.sp.get()),self.wholeseller.get()]
			r=csv.writer(f)
			r.writerow(data)
		l[0] += (str(self.item.get()) +'\n')
		l[1] += (str(self.stock.get()) + "\n")
		l[2] += (str(self.sp.get()) + '\n')
		l[3] += (str(self.cp.get()) + '\n')
		l[4] += (str(self.wholeseller.get()) + '\n')
		self.lab_item.configure(text=l[0])
		self.lab_stock.configure(text=l[1])
		self.lab_cp.configure(text=l[2])
		self.lab_sp.configure(text=l[3])
		self.lab_seller.configure(text=l[4])
		item_data = biller.itemdata_reader()