
import csv


from datetime import date
from home_window import *


frames=[]

customer_dat ={}
def custfresher():
	global customer_dat
	with open('Data_files\\customer_file.csv',newline='\n') as cust:
		alldata = csv.reader(cust,delimiter=',')
		for i in alldata:
			customer_dat[i[0]] = i[1]
			
custfresher()


if __name__ == "__main__":
	h = home()
	h.add_billing()
	h.stock_item_adder()
	h.mainloop()


