k = int(input("Enter the value"))

i = 1

while i <= k:
    j=1
    starting_letter = chr(ord('A') + i -1)

    while j <= k:
        character = chr(ord(starting_letter) + j -1)
        print(character,end="")
        j = j+1
    print()
    i = i +1