def search(ar,key):
    for i in range(len(ar)):
        pos=-1
        if key==ar[i]:
            pos=i
            print(f"Item found at {pos}")
            break
    else:print("Item not found")
ar=[1,4,5,7,8,9]
key=int(input("Enter the number"))
search(ar,key)