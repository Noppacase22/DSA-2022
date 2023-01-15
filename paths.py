# Week 12 Quiz,
# Question 9

# Solved by ChatGPT
# Basically just Fibonacci

def num_paths(n):
  # create a list to store the number of ways to get to each vertex
  ways = [0] * (n+1)

  # base case: there is only 1 way to get from vertex 1 to vertex 2,
  # and 2 ways to get from vertex 1 to vertex 3
  ways[2] = 1
  ways[3] = 2

  # calculate the number of ways to get to each subsequent vertex
  # using the values stored in the ways list
  for i in range(4, n+1):
    ways[i] = ways[i-1] + ways[i-2]

  # return the number of ways to get to the last vertex
  return ways[n]

# test the function
print(num_paths(5))  # should print 5
print(num_paths(10))  # should print 55
print(num_paths(20))