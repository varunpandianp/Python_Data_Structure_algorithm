# Problem statement
# Print the following pattern for the given number of rows.
#
# Note: N is always odd.
#
#
# Pattern for N = 5
#
#
#
# The dots represent spaces.

# N=int(input())
# i = 0
# while i <= (N+1) // 2:
#     j=1
#     spaces=1
#     while spaces <= N -i:
#             print(" ",end="")
#             spaces=spaces+1
#     stars=2*i-1
#     while j <= i:
#         print("*",end="")
#         j=j+1
#     p=j
# #     while p >= i:
# #         print("*",end="")
# #         p=p-1
#     print()
#     i=i+1

# N=int(input())
# i=1
# mid =N//2+1
# while i<=mid:
# #     space= N - i
#     j=1
#     while j<= N-i:
#         print(" ",end="")
#         j=j+1
#     star=1
#     while star <= 2*i-1:
#         print("*",end="")
#         star=star+1
#     print()
#     i=i+1
# i=mid-1
# while i >=1:
#      space = N-i
#      j=1
#      while j <= space:
#          print(" ",end="")
#          j=j+1
#      star =1
#      while star <=2*i-1:
#          print("*",end="")
#          star=star+1
#      print()
#      i=i-1

N=int(input())
i=1
mid = N//2+1
while i<=mid:
    j=1
    while j<=mid-i:
        print(" ",end="")
        j=j+1
    star=1
    while star<=2*i-1:
        print("*",end="")
        star=star+1
    print()
    i=i+1

i=mid-1
while i >=1:
    j=1
    while j<=mid-i:
        print(" ",end="")
        j=j+1
    star=1
    while star <= 2*i-1:
        print("*",end="")
        star=star+1
    print()
    i=i-1