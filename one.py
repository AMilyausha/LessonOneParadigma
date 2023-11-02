def sortMassivImperative(arr):
    flag = True
    while flag:
        flag = False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = True
    return arr

def sortMassivDeclarative(arr):
    arr.sort(reverse=True)
    return arr


print(f"Imperative style -> {sortMassivImperative([35, 9, 2, 7, -4, 2, 3, 78])}")
print(f"Declarative style -> {sortMassivDeclarative([35, 9, 2, 7, -4, 2, 3, 78])}")