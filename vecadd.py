from multiprocessing import pool


def multiply(pair):
	a, b = pair
	return a*b
if __name__ = "__main__":	
	v1 = list(map(int, input("Enter the element of first vector").split()))
	v2 = list(map(int, input("Enter the element of second vector").split()))



def multiply(pair):
	
	a, b = pair
	return(a*b)
	
if __name__ == "__main__":
	v1 = list(map(int, input("Enter the element of first vector").split()))
	v2 = list(map(int, input("Enter the element of second vector").split()))
	
	if len(v1) != len(v2):
		print("Error")
	else:
		with pool() as pool:

	
			result = pool.map(multiply , zip(v1, v2))
			dot_product = sum(result)
			print("dot product (parallel) :", dot_product)
			result = pool.map(multiply, zip(v1, v2))
			dot_product = sum(result)
			print("dot product (parallel) :", dot_product)

	
