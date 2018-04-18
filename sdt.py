def rule(num):
	c = 0
	for i in num:
		if num.count(i)>c:
			c = num.count(i)
			t = i
	if c>4: return False
	elif c==4:
		if num.rfind(t)-num.find(t)==4: return False
		else: return True
	else: return True
header = [	96, 97, 98, 86, 162, 163, 164, 165, 166, 167, 168, 169,	#viettel
			91, 94, 88, 123, 124, 125, 127, 129,					#vinaphone
			90, 93, 89, 120, 121, 122, 126, 128,					#mobifone
			92, 188, 186]											#vietnamobile
#f = open("sdt.txt",mode="w")
for n in range(1011,10**7):
	num = str(n).rjust(7,'0')
	for h in header:
		if rule(num):
			#f.write("0"+str(h)+num+"\n")
			print("0"+str(h)+num)
#f.close
"""Luat: tao ra cac sdt (chi tinh phan than, ko tinh dau so) sao cho:
- Toi da 4 chu so giong nhau.
- Toi da 3 chu so giong nhau lien nhau.
Cach dung: lua chon in ket qua ra man hinh (dong 22) hoac in ra file (21,16,23).
"""
