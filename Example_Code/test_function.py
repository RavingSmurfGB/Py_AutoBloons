import time

lvl_detected = False


def click():
	if lvl_detected == True:
		return
	print("i clicked")



def game_function():
	if lvl_detected == True:
		return
	print(" game was ran")
	if lvl_detected == True:
		return
	click()


while True:

	if lvl_detected == False:
		game_function()
		# you would put all main game funcitons in here!

		time.sleep(1)

	time.sleep(1)

'''
if lvl_detected == True: # you would put this as many times around stuff in functions as possible!
		return # This will exit out of the funciton it is ran in immediatly
'''