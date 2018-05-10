#IanNolon
#5/10/18
#howManyWords.py

file = open('engmix.txt')

nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for word in file:
    nums[len(word.strip())] += 1
print(nums)
