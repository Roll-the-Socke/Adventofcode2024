import re



    
def find_numbers(string):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, string)
    return [[int(num) for num in nums] for nums in matches]

def calculation(nums):
    sum = 0
    for a, b in nums:
        sum += a * b
    return sum 

def main():
    with open("input.txt") as input:
        string = input.read()
    matches = find_numbers(string)
    print(calculation(matches))

if __name__ == "__main__":
    main()