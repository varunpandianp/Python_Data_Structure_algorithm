# Problem statement
# Create a function that determines whether a given number N belongs to the Fibonacci sequence. If N is found in the Fibonacci sequence, the function should return true; otherwise, it should return false.
#
#
#
# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 0 <= n <= 10^4
# Sample Input 1 :
# 5
# Sample Output 1 :
# true
# Explanation :
# Fibonacci sequence begins 0, 1, 1, 2, 3, 5, ... and so on. Since 5 appears in the sequence.

def checkMember(n):
    # write your code logic here !!!!
	a=0
	b=1

	while a <=n:
		if a==n:
			return True
		c=a+b
		a=b
		b=c

	return False
