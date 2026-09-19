# Problem statement
# Print the following pattern for the given number of rows.
#
# Pattern for N = 4
# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444

N = int(input())

#upperhalf
for i in range(N):

    # Left side
    for j in range(N, N - i , -1):
        print(j, end="")

    # Middle
    for j in range(2 * (N - i) - 1):
        print(N - i, end="")

    # Right side
    for j in range(N - i+1, N + 1):
        print(j, end="")

    print()

#lowerhalf

for i in range(N-2,-1,-1):

    # Left side
    for j in range(N, N - i , -1):
        print(j, end="")

    # Middle
    for j in range(2 * (N - i) - 1):
        print(N - i, end="")

    # Right side
    for j in range(N - i+1, N + 1):
        print(j, end="")

    print()

