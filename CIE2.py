n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter the elements: ").split()))
if arr == arr[::-1]:
    print("Perfect Array")
else:
    print("Not a Perfect Array")