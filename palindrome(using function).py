def palindrome(num):
    num_str=str(num)
    reversed_str=num_str[::-1]
    if num_str==reversed_str:
        return True
    else:
        return False
num=int(input("Enter a number to check for palindrome:"))
if palindrome(num):
    print(num,"is palindrome")
else:
    print(num,"is not a palindrome")