import concurrent.futures
import time

def targ_func(args):
	print(f'EXECUTING THREAD {args}')
	time.sleep(2)
	print(f'STOPPING THREAD {args}')

if __name__ == '__main__':
	with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
		executor.map(targ_func, range(3))