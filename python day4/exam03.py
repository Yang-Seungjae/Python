def remove_vowels(input_str):
    vowels = "aeiouAEIOU"  # 대소문자 모음
    result = ''.join([char for char in input_str if char not in vowels])
    return result

input_str = "i am a boy"
result_str = remove_vowels(input_str)
print(result_str)



data = set(input('문장을 입력하세요'))
print(data)
data2=[s for s in data if s not in 'aeiouAEIOU']

print(data2)
