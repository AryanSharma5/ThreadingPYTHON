# This is a normal thread. After the thread completes its 
# execution then only program will be able to exit.

import threading
import time

'''
def targ_func(name):
	print(f'starting thread {name}')
	time.sleep(2)
	print('finishing....', sep = '\n')

if __name__ == '__main__':
	print('before creation....')
	t = threading.Thread(target = targ_func, args = ('aryan',))
	print('before starting....')
	t.start()
	print('program waiting thread to complete its execution....')
'''

# DEAMON THREADS : DEAMON is any process that runs in background.
# Program does not wait for deamon thread to complete its execution.

def targ_func(name):
	print(f'starting thread {name}')
	time.sleep(2)
	print('finishing....', sep = '\n') # This will not be printed....
									   # coz Program terminates before 
									   # thread completes its execution.

if __name__ == '__main__':
	print('before creation....')
	t = threading.Thread(target = targ_func, args = ('aryan',), daemon = True)
	print('before starting....')
	t.start()
   	t.join() # This func will make main thread to wait for thread t to complete its 
   	         # execution.
	print('program waiting thread to complete its execution....')