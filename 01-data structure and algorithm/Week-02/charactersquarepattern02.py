k = int(input("enter the value:"))

i =1

while i <= k:
    j=1
    starting_char="A"
    while j <= k:
        character=chr(ord(starting_char)+j-1)
        print(character,end="")
        j = j+1
    print()
    i = i+1