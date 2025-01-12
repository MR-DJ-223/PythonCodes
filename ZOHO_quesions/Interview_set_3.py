


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
    
