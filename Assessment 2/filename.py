#Coding question 3:
def sort_square(arr, n):
    for i in range(n):
        arr[i] = arr[i] * arr[i]
    arr.sort()


arr = [1, 2, 3, 5, 6, 8, 9]
n = len(arr)
print("\n")
sort_square(arr, n)
print("sorted arrey")
for i in range(n):
    print(arr[i], end=" ")

# Coding Question 9:
nums = [3, 4, -4, 10, 11, -1, 6]
target = 16


def find_pair(numbers, target_sum):
    for i in range(len(numbers) - 1):
        for k in range(i + 1, len(numbers)):
            if nums[i] + nums[k] == target_sum:
                print((nums[i], nums[k]))
                return

    print('Pair not found')


if __name__ == '__main__':
    find_pair(nums, target)
