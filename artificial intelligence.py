# python artificial intelligence
question = input('ask a question ')

def tell_answer():
		if question == input('How are you?'):
			How_are_you_qn = input("I'm alright,how are you? ")
			if How_are_you_qn == 'Good':
				print('Good')
			elif How_are_you_qn == 'bad':
				print('Oh no!')
			else:
				print("I don't Know what you mean. Is your grammar correct? if it is, my brain doesn't understand.")
				
		elif question == 'Do you like coding?':
			print("Yes, I love coding, it's the best thing in the world!")
		else:
			print("I don't Know what you mean. Is your grammar correct? if it is, my brain doesn't understand.")
tell_answer()
	
