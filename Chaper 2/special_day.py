month = int(input())
date = int(input())

if month < 2 or (month == 2 and date < 18):
	print('Before')
elif ((month == 2) and (date == 18)):
	print('Special')
else:
	print('After')
