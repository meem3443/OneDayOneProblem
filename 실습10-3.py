while True:
    filename = input("파일 이름을 입력하세요.")

    try:
        infile = open(filename, "r")
        
    except IOError:
        print("파일이 존재하지 않습니다.")

    else:
        print("파일이 열렸습니다")
        infile.close()
        break