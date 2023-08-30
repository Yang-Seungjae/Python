'''
    input.txt 읽어서 다음의 결과를 출력하시오
    1. 총 단어의 개수 세어보기
    2. 단어의 빈도수 (알파벳순으로 출력)

          a  15
        above 1
    3. 단어가 몇번째 라인에 나왔는지 출력
      a 15  2,3,5,11,11,20,22
'''

with open('input.txt', 'r') as file:
    line = file.readline().split(' ')
    while line != '':
        print(line)
        line = file.readline().rstrip('\n')