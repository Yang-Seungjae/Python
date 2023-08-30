def print_book(title, writer, price):
    print(f'제목 : {title}')
    print(f'글쓴이 : {writer}')
    print(f'가격 : {price}')
    pass

print_book('홍길동전','허균',15000)
print_book(title='홍길동전', writer='허균',price=15000)
print_book(price=15000,writer='허균', title='홍길동전')


book = {'title' : '홍길동전', 'writer':'허균', 'price':15000}

print(*book) # 딕셔너리 언팩킹 근데 딕셔너리는 키밸류값이므로 *을 하나만 붙이면 key만 언팩킹된다

print_book(**book)# 밸류언팩킹를 의미


def print_book_info(**args):    # 가변인자형으로 딕셔너리 사용 가능
    # 딕셔너리 출력을 위해서는 keys 함수나 values 함수나 둘다 가지는 items 함수를 사용한다
    for key, value in args.items():
        print(f'{key} : {value}')
        print('=' * 20)

print_book_info(title='홍길동전',writer='허균',price=15000)

print_book_info(**book)