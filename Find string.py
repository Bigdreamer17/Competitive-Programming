def count_substring(string, sub_string):
    return string.find(sub_string)
if __name__ == '__main__':
    string = input("Enter the string: ").strip()
    sub_string = input("Enter the sub-string: ").strip()
    
    count = count_substring(string, sub_string)
    print(count)
