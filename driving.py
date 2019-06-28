contry = input('whitch contry ?')
age = input('age:')
age = float(age)
if contry =='taiwan':
	if age >= 18:
		print('get a linesnce')
	else:
		print('no drive')
elif contry =='germany':
	if age >= 15:
		print('get a linesnce')
	else:
		print('no drive')
else:
	print('input taiwan or germany')