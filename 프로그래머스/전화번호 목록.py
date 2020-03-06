def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):       # startswith(시작하는 문자, 시작지점, 끝나는지점)
            return False            # endswith(끝나는 문자, 시작지점, 끈나는지점)
    return True

phone_book = ['119', '97674223', '1195524421']
solution(phone_book)