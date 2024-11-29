arr= [5, 5, 4, 1,3,2]
n = len(arr)

def secondlargest(arr,n):
    first_lar = float("-inf")
    second_lar = float("-inf")

    for i in range(n):
        if arr[i] > first_lar:
            second_lar = first_lar
            first_lar = arr[i]
            
        elif arr[i]> second_lar and arr[i] != first_lar:
            second_lar = arr[i]
    print(second_lar)

secondlargest(arr,n)