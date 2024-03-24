def knapsack(n: int, capacity: int, weights: list[int], profit: list[float]) -> int:
	# create a 2D matrix that stores how much profit we can accrue using all items ranging from 0-row.
	# for example, first row states what is the profit we can use bag capacity of 0, 1, 2, 3 and so on.
	# row 2 denotes how much profit can we make using both item 1 and 2 and with bag capacity of 0, 1, 2, 3 and so on.
	# naturally, using 0 (row) items means we cannot make any profit. Similarly, 0th column means profit with bag
	# capacity = 0 => 0 profit for however many items you got.
	dp = [0 for _ in range(capacity+1)]

	# for all items 1 through n
	for item in range(1, n+1):
		# we only need the previous row to remember the maximum profit using one less item. We can use that
		# to compute the next row, so in order to prevent overwriting of values while use the same array, iterate in reverse
		# for each of the partial_capacity in reverse order (stop at 0 since no need to check it)
		for partial_capacity in range(capacity, 0, -1):
			# consider this item only if the weight of the item is less than the bag capacity. -1 because we are indexing from 1
			if weights[item - 1] <= capacity:
				# the max profit will be calculated by either using this item or not using.
				# if we don't use it, then it will simply be whatever the old profit was.
				# if we use it, then it will be simply value of that item + (max profit by subtracting item weight from bag capacity
				# and checking our dp table for the profit that we could make from the remaining bag capacity)
				dp[partial_capacity] = max(dp[partial_capacity], profit[item - 1] + dp[partial_capacity - weights[item-1]])
	return dp[capacity]

if __name__ == '__main__':
	profit = [60, 100, 120]
	weights = [10, 20, 30]
	capacity = 50
	n = len(profit)
	print(knapsack(n, capacity, weights, profit))