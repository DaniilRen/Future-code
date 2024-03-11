import time

# task 1
def count_time(iter):
	def inner_decorator(func):
		def wrapper(**kwargs):
			overall_time = 0
			for i in range(iter):
				start = time.perf_counter_ns()
				func(kwargs['x'])
				time_ = time.perf_counter_ns() - start
				overall_time += time_
				print(f'time on iter {i}: {time_} ns')
			print(f'average time for {iter} iter: {overall_time / iter}')
			return True
		return wrapper
	return inner_decorator

@count_time(iter=10)
def f(x):
	return x / 212324 * 124375757232.232328

f(x=42)


# task 2
'https://github.com/DaniilRen/CF_repo'
