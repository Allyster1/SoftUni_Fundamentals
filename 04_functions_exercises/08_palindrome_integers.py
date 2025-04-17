def isPalindrome(string_number: str) -> bool:
    if string_number == string_number[::-1]:
        return True
    return False


palindrome_string = input().split(', ')

for i in palindrome_string:
    print(isPalindrome(i))
