def palindrome(nums):
    for num in nums:
        reversed_num = num[::-1]
        if num == reversed_num:
            print("True")
        else:
            print("False")


numbers = input().split(", ")

palindrome(numbers)