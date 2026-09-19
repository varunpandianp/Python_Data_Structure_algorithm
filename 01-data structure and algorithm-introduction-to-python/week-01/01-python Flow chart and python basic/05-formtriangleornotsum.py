# /*You are given 3 numbers. Each number represents the length of a line. You need to figure out whether these lines can form a valid triangle.
#
# If a valid triangle can be formed, print "Yes", otherwise print "No".
#
# Draw a flowchart for this process
#
# A triangle is a valid triangle, If and only If, the sum of any two sides of a triangle is greater than the third side. For Example, let A, B and C are three sides of a triangle. Then, A + B > C, B + C > A and C + A > B
#
# Note : You don't need to submit the problem. Just attempt in your notebook and ask doubts if you need help.


a = 5
b = 7
c = 10

if a+b>c and a+c>b and b+c>a:
    print("its valid traingle")
else:
    print("it wont print valid traingle")
