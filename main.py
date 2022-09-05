
import csv


from datetime import date
from home_window import *


frames=[]

customer_dat ={}

if __name__ == "__main__":
	h = home()
	h.add_billing()
	h.stock_item_adder()
	h.mainloop()


