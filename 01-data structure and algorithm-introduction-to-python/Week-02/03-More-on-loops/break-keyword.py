n = int(input())
k = 2
while k <=n:
     d=2
     flag = False
     while d<k:
         if k % d ==0:
             flag = True
             break
         d=d+1
     if (not(flag)):
         print(k)
     k=k+1



     Equivalent code using for loops
     n = int(input())

     for k in range(2, n + 1):
         flag = False

         for d in range(2, k):
             if k % d == 0:
                 flag = True
                 break

         if not flag:
             print(k)