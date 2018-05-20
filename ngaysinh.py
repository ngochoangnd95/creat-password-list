f = open("ngaysinh.txt","w")
for year in range(1960,2019):
	Nhuan = False
	if(year%4==0 and year%100!=0):
		Nhuan = True
	for month in range(1,13):
		for day in range(1,32):
			checkMonth = False
			for m30d in [4,6,9,11]:
				if(month==m30d):
					checkMonth = True
			if(month==2 and ((Nhuan==True and day>29) or (Nhuan==False and day>28))):
				pass
			elif(checkMonth==True and day==31):
				pass
			else:
				f.write(str(day)+str(month)+str(year)+'\n')
				if(day<10):
					d = str(day).rjust(2,'0')
				else:
					d = str(day)
				if(month<10):
					m = str(month).rjust(2,'0')
				else:
					m = str(month)
				f.write(d+m+str(year)+'\n')
f.close()