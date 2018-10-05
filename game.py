a=['1','2','3','4','5','6','7','8','9']

def print_board():
	print(a[0],'|',a[1],'|',a[2])
	print('----------')
	print(a[3],'|',a[4],'|',a[5])
	print('----------')
	print(a[6],'|',a[7],'|',a[8])
import random
player1turn=True
while True:
	print_board()
	x=input('where to put x?:')
	if(x in a):
		if(a[int(x)-1]=='x' or a[int(x)-1]=='0'):
			print('snap! place taken! choose another one!')
			continue
		else:
			if player1turn:
			    a[int(x)-1] ='x'
			    player1turn = not player1turn
			else:
				a[int(x)-1] ='0'
				player1turn =not player1turn
		    	for i in (0,3,6):
					if(a[i] == a[i+1] and a[i] == a[i+2]):
						print('game over')
						exit()
				for i in range(3):
				if(a[i] == a[i+3] and a[i] == a[i+6]):
				print_board()
				print('game over')
				exit()


	
		
