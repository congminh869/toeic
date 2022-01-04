import numpy as np
import random
def one_lession(data, index, index_lession):
	if index != 0: # select lession
		lession_data = data[index_lession[index-1]: index_lession[index]]
		print('bạn đã chọn ', lession_data[0])
		while True:
			# try:
			i = random.randint(1, len(lession_data)-1)
			if len(lession_data[i]) == 0:
				continue
			else:
				print(lession_data[i].split('/')[0])
				answer = input()
				if answer == 'exit':
					break
				print(lession_data[i])
				print('---------------------------------------------')
	else: #random lession
		pass
	main()

def many_lession(data, index, number_of):
	if index == 0: # select lession
		pass
	else: #random lession
		pass
def main():
	with open ("all_lession.txt", "r") as myfile:
		data = myfile.read().splitlines()

	Lesson = 1
	index_lession = []
	count = 0
	for i in data:
		Lesson = i.find('Lesson')
		if int(Lesson) == 0 :
			print(i)
			index_lession.append(count)
			Lesson = 1
		count = count +1

	print('1. chọn 1 lession (số lession - 0 random)'.center(20, "-"))

	while True:
		index = int(input('chon 1 lession hoặc nhấn 0 để random: ')) 
		if index==0:
			index = random.randint(1, 50)
		if index>0 and index<=50:
			break

	

	one_lession(data, index, index_lession)

if __name__ == "__main__":
	main()
