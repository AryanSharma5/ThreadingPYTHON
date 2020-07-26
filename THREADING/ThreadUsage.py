import threading
import time

def targetFunction(name, sleepTime, threads = False):
	iteration = 'Thread' if threads else 'Iteration'
	print(f'Hi! I am {name} {iteration}, Going to sleep....')
	time.sleep(sleepTime)

print('RUNNING FUNCTION FOR 5 ITERATIONS, EACH ITERATION WILL CONSUME 5 SECONDS TO COMPLETE....')

start = time.time()
for i in range(5):
	targetFunction(i, 5)
end = time.time()
print(f'TIME CONSUMPTION: {end - start}')

print('RUNNING FUNCTION 5 TIMES USING THREADS, EACH THREAD WILL SLEEP FOR 5 SECONDS....')

start = time.time()
threadsList = []
for i in range(5):
	thread = threading.Thread(target = targetFunction, name = i, args = (i, 5, True))
	thread.start()
	threadsList.append(thread)
for thread in threadsList:
	thread.join()
end = time.time()
print(f'TIME CONSUMPTION: {end - start}')