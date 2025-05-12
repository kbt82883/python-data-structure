from ListByClass import ArrayList

list = ArrayList()
while True:
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료-> ")

    if command == 'i':  # 입력
        try:
            pos = int(input("  입력행 번호 : "))
            str = input("  입력행 내용 : ")
            list.insert(pos, str)
        except:  # 입력행 번호에 정수가 아닌 값을 입력할 때
            print("Insert Fail")
    
    elif command == 'd':  # 삭제
        try:
            pos = int(input("  삭제행 번호 : "))
            list.delete(pos)
        except:  # 삭제행 번호에 정수가 아닌 값을 입력할 때
            print("Delete Fail")

    elif command == 'r':  # 변경
        try:
            pos = int(input("  변경행 번호 : "))
            str = input("  변경행 내용 : ")
            list.array[pos] = str
        except:  # 변경행 번호에 정수가 아닌 값을 입력할 때
            print("Replace Fail")

    elif command == 'p':  # 출력
        print("Line Editor")
        for i in range(list.size):  # 0 ~ 배열길이만큼 반복
            print('[ %d] %s' % (i, list.array[i]))

    elif command == 'l':
        try:
            with open("test.txt", "r") as f:
                pos = 0
                for str in f.readlines():
                    list.insert(pos, str.strip())
                    pos += 1
        except:  # 경로에 test.txt 파일이 존재하지 않을 때
            print("Please save first")

    elif command == 's':
        with open("test.txt", "w") as f:
            for i in range(list.size - 1):
                f.write(list.array[i] + '\n')
            f.write(list.array[list.size - 1])

    elif command == 'q':
        break
