
"""
generate a python file for the following requirements:
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:
               0,1,2,3,4
Input: nums = [2,3,1,1,4]

Output: true

Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
               0,1,2,3,4
Input: nums = [3,2,1,0,4]

Output: false

Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

def can_jump(nums):
 
    for i in range(len(nums)):
        if ((nums[i]+i+1) == len(nums)):            
            return True
    return False 

if __name__ == "__main__":
    nums_input = input("Enter the array of numbers separated by spaces: ")
    nums = list(map(int, nums_input.strip().split()))
    result = can_jump(nums)
    print("Can reach last index:", result)
