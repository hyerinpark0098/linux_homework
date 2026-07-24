'''
- **퀴즈 프로그램 만들기 (주제 : 리눅스 명령어)**
- 조건문,반복문,리스트 사용할 것 v
- 문제는 최소 5문제 이상 준비할 것 v
(문제로는 명령어의 설명을 주고, 정답은 명령어를 맞히도록)
- 5문제 중 랜덤으로 3문제 뽑아서 출제할 것v
- 문제 유형은 모두 주관식으로 할 것 v
- 정답은 대소문자 구분없이 정답처리 가능하도록 할 것 v
- 정답을 못 맞추면, 바로 정답을 알려줄 것 v
- 마지막에 총 몇문제 맞추었는지 알려줄 것v
- 맞춘 문제 수에 따라 등급 출력 (A,B,C,F)v
- 게임 종료 후 재시도 할 수 있게 만들어줄 것
- 유저 입력으로 게임을 그만할 수 있게 만들어줄 것 (프로세스 종료)
- 커밋은 최소 2개 이상 찍을 것
'''

import random

#퀴즈 데이터베이스 (질문, 정답)
quiz_list = [
    ("현재 내가 위치해 있는 폴더의 절대 경로를 출력해 주는 명령어는?", "pwd"),
    ("현재 폴더 내의 파일 및 폴더 목록을 확인하는 명령어는?", "ls -al"),
    ("새로운 폴더를 생성할 때 사용하는 명령어는?" , "mkdir"),
    ("텍스트 파일의 내용 전체를 터미널 화면에 바로 출력하는 명령어는?" , "cat"),
    ("파일이나 폴더를 삭제할 때 사용하는 명령어는?" , "rm"),
    ("파일을 이동할 때 사용하는 명령어는?" , "mv"),
    ("원하는 폴더로 이동(위치 변경)할 때 사용하는 명령어는?" , "cd"),
    ("현재 폴더에 있는 \'hello.txt\' 파일 하나를 삭제하는 명령어를 작성하세요." , "rm hello.txt"),
    ("\'documents\'라는 이름의 빈 폴더를 삭제하는 명령어를 작성하세요." , "rm -r documents"),
    ("vi로 생성한 txt에서 작성 중인 내용을 저장하고 종료하는 명령어는?" , ":wq"),
    ("\'kh\' 폴더 안에 있는 \'hello.txt\' 파일을 \'/content/kh2\' 폴더 내부로 이동시키는 명령어를 작성하세요" , "mv hello.txt /content/kh2")
]

while True:

    count = 0
    score = 0

    print("리눅스 명령어 퀴즈 게임을 시작합니다! 야호~")
    print()
    while count <3:

        data = random.choice(quiz_list)

        qui01 = data[0]
        ans =data[1]

        print(qui01)
        answer = input("정답:").lower()

        if ans == answer:
            print("정답")
            count += 1
            score += 1
        else :
            print(f"틀렸습니다. 정답은 \"{ans}\" 입니다.")
        count += 1

    if score == 0 :
        grade = "F"
    elif score ==1 :
        grade = "C"
    elif score ==2 :
        grade = "B"
    elif score ==3 :
        grade = "A"

    print("퀴즈가 끝났습니다. 고생하셨습니다!")
    print(f"총 3문제 중 \"{score}\"문제를 맞췄습니다")
    print (f"{score}문제를 맞춰 당신은 \"{grade}\"등급 입니다.")

    while True:
        again = input("게임을 그만하시겠습니까?[yes or no] :").lower()
        if again not in ["y", "n", "yes", "no"]:
            print("'yes' or 'y' 또는 'no' or 'no' 만 입력할 수 있습니다. 다시 입력해 주세요.")
        else:
            break

    if again not in ["n", "no"]:
        print("게임을 종료합니다. 이용해주셔서 감사합니다.")
        break
    else:
        continue


