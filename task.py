def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


input_str = "hello"
output_str = reverse_string(input_str)
print(output_str)  
