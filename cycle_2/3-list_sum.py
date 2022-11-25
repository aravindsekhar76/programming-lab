def list_sum_fun(l):

	total = 0

	for i in l:

		total += i

	return total

l = input("Enter List :").split(" ")

l = list(map(int, l))

print(list_sum_fun(l))
