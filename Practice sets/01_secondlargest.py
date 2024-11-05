arr= [5, 5, 4, 1,3,2]
n = len(arr)

def secondlargest(arr,n):
    #giving both the variable as -ve infinity such that arr[] values can easily replaced with largest +ve values
    first_lar = float("-inf")
    second_lar = float("-inf")

    for i in range(n):
        if arr[i] > first_lar:
            second_lar = first_lar
            first_lar = arr[i]
        # arr[i] != helps in not considering duplicates value    
        elif arr[i]> second_lar and arr[i] != first_lar:
            second_lar = arr[i]
    print(second_lar)

secondlargest(arr,n)
