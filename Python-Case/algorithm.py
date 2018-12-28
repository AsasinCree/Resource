# greatest common divisor 最大公约数
# short division 短除法
a, b = map(int, input('Enter two integers : ').split())
r = 1
i = 2
while i <= a and i <= b:
    while a % i == 0 and b % i == 0:
        r *= i
        a /= i
        b /= i
    i += 1
print(r)


# m = int(input())4 10
# print(m)


def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

最短路径问题 Dijkstra 迪杰斯特拉