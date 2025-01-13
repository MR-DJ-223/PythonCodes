


def expand_string():
    '''
    Eg 1: Input: a1b10
       Output: abbbbbbbbbb
Eg: 2: Input: b3c6d15
          Output: bbbccccccddddddddddddddd
The number varies from 1 to 99.
    '''
    
    import re

    input = 'b3c6d15'
    pattern = r'([a-zA-Z])(\d+)'

    matches = re.findall(pattern, input)

    # print(matches)
    result = ''.join(char*int(num) for char, num in matches)
    print(result)


def custom_sort():
    '''
    Eg 1: Input: 13,2 4,15,12,10,5
        Output: 13,2,12,10,5,15,4
    Eg 2: Input: 1,2,3,4,5,6,7,8,9
        Output: 9,2,7,4,5,6,3,8,1 

    '''
    input = '13,2,4,15,12,10,5'
    nums = input.split(',')
    odd = []
    even = []
    for i in nums:
        if int(i)%2 == 0:
            even.append(int(i))
        else:
            odd.append(int(i))
    
    odd.sort(reverse=True)
    even.sort()
    
    result=[]
    max_len = min(len(odd), len(even))
    for i in range(max_len):
        result.append(odd[i])
        result.append(even[i])
    if len(odd) > len(even):
        result.extend(odd[max_len:])
    elif len(even) > len(odd):
        result.extend(even[max_len:])
    print(result)
    

def custom_pattern():
    '''
    Eg 1: Input: 12345
       Output:
        1       5
        2   4
            3
        2  4
        1      5
        '''
    input = '12345'
    max_len = len(input)
    for i in range(max_len):
        for j in range(max_len):
            if j == i or j == max_len-i-1:
                print(input[j], end='')
            else:
                print(' ', end='')
        print()


def check_sub_string():
    '''
    Having 3 functions init, call each function and print the output
    Eg 1:Input:
    String 1: test123string
    String 2: 123
    Output: 4
    '''

    input = 'test123string'
    sub_str = '1234'
    def method_1():
        print(f"printing from method 1")
        if sub_str in input:
            print(input.index(sub_str))
        else:
            print('Substring not found')
            print(-1)
    
    def method_2():
        print(f"printing from method 2")
        ptr2 = 0
        count = 0

        for char in input:
            # If characters match, move the pointer of String 2
            if ptr2 < len(sub_str) and char == sub_str[ptr2]:
                ptr2 += 1
            # If String 2 is fully matched
            if ptr2 == len(sub_str):
                count += 1  # Increment the count
                ptr2 = 0  # Reset pointer to start checking for the next occurrence
        print(count)
    
    def method_3():
        import re
        print(f"printing from method 3")
        matches = re.findall(sub_str, input)
        print(matches) 
    
def merged_array():
    '''
    Eg 1: Input:
    Array 1: 2,4,5,6,7,9,10,13
    Array 2: 2,3,4,5,6,7,8,9,11,15
    Output:
    Merged array: 2,3,4,5,6,7,8,9,10,11,13,15 
    '''
    input1 = "2,4,5,6,7,9,10,13"
    input2 = "2,3,4,5,6,7,8,9,11,15"
    arr1 = input1.split(',')
    arr2 = input2.split(',')
    print(sorted(list(map(int,(set(arr1+arr2))))))


def reverse_string():
    '''
    Eg 1: Input: one two three
      Output: three two one
    Eg 2: Input: I love india
      Output: india love I 
      '''
    input1 = "one two three"

    arr = input1.split(" ")
    # arr.sort()
    # print(arr)
    print(" ".join((arr[::-1])))
reverse_string()



   

    

