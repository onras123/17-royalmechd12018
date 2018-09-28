import random

a={1:'scissor',2:'papper',3:'rock'}

while True:
	p=input("your choice s/p/r: ")

	c=a[random.randint(1,3)]

	print("you chose:",p,"computer chose:",c)

	if(p==c):
		print('draw!')
	elif(p=='rock' and c=='papper'):
		print('you lose!')
	elif(p=='papper' and c=='scissor'):
		print('you lose!')
	elif(p=='scissor' and c=='rock'):
		print('you lose')
	elif(p=='rock' and c=='scissor'):
		print('you win')
	elif(p=='papper' and c=='rock'):
		print('you win')
	elif(p=='scissor' and c=='papper'):
		print('you win')
	else:
		exit()