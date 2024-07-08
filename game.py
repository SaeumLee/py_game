

# TODO STEP 0
is_dev_mode = False #플래그 변수, 값의 변화에 따라 흐름제어가 변화된다
game_title = 'Number Matching Game' if is_dev_mode else None
player_name = 'Guest' if is_dev_mode else None

# TODO step 1-1. 리소스 정리
#리소스 (이미지, 문자열 수치값등) 는 코드 외부에서 관리하는게 적절

GAME_TITLE_MAX_LENGTH = 28 # 가변을 부여해서 프로그램을 유기적으로 조정 할수 있다.

#\ 표식을 사용하면 한라인이 길었을때 끊어서 표현이 가능함
msg = f'게임 제목을 입력해 주세요. 최대{GAME_TITLE_MAX_LENGTH}자 이내(<=28),\ 영문/숫자 조합으로 입력하세요\n\n >'

err_msg = '정확하게 입력하세요'

# step 1-2 기능 구현
while not is_dev_mode: #무한대기에 대한 별도 조건이 없었으므로 참(False상황의 반대)으로 처리
    # 프럼프트가 출력되고 나서 게임 제목을 입력받는다.
    # input() 사용자가 엔터를 칠떄까지 무한대기
    game_title = input (msg).strip() # 사용자 입력을 받으면 무조건 공백 제거 수행
    # 값 검사 -> 3가지 상황으로 분류 상활별로 분기 처리 ->if
    # 비어있는 문자열 => 조건식 => False => 이 상황(부정적 상황)을 잡아낸다 => not
    if not game_title: # 사용자가 아무런 입력없이 엔터 -> 메시지 던지고 -> 다시 입력 대기 -> 무한히 대기 -> while
        print(err_msg)
    elif len(game_title) > GAME_TITLE_MAX_LENGTH: 
        # 커스텀 메시지 -> 초과된 수 표현 -> 포멧팅
        print(f'''게임 제목을 정확하게 입력하세요.
              최대 {GAME_TITLE_MAX_LENGTH} 이내로 입력하시고,
              방금 입력하신 내용은 {game_title} 이고,
              최대길이 대비 {len(game_title)-GAME_TITLE_MAX_LENGTH}자가 초과 되었습니다.
        ''')       
    else:
        break

print(f'step1 완료, 게임 제목은 = {game_title}')

# TODO step2 : 기능 구현 step1과 동일하게, 진행 continue 사용

player_name_MAX_LENGTH = 28 # 가변을 부여해서 프로그램을 유기적으로 조정 할수 있다.


player_name_1 = f'플레이어의 이름을 입력해 주세요. 최대{player_name_MAX_LENGTH}자 이내(<=28),\ 영문/숫자 조합으로 입력하세요\n\n >'

err_msg2 = '정확하게 입력하세요'

while not is_dev_mode: 
    player_name = input (player_name_1).strip() 
    if not player_name: 
        print(err_msg2)
        continue
    if len(player_name) > player_name_MAX_LENGTH: #elif도 여기서는 ok
        print(f'''게임 제목을 정확하게 입력하세요.
              최대 {player_name_MAX_LENGTH} 이내로 입력하시고,
              방금 입력하신 내용은 {player_name} 이고,
              최대길이 대비 {len(player_name)-player_name_MAX_LENGTH}자가 초과 되었습니다.
        ''')       
        continue
    #코드가 여기까지 진행되면 반복문을 중단(탈출)한다
    break

print(f'step2 완료, 플레이어 이름은 = {player_name}')


# TODO step3. 
'''
현재까지 생성된 변수를 활용하여 게임 타이틀 프럼프트 출력
총칸은 32칸
-(1칸) + 공백(1칸) + 글자(28칸) + 공백(1칸) + -(1칸)
글자는 중앙정렬
제목 -
이름 -
ver.1.0.0 -

'''
# step 3-1 리소스 정의

Game_icon = '-'
Game_space = 2
Game_space_2 = 2
Game_icon_max_line = 28 + Game_space + Game_space_2
Game_version = 'ver 1.0.0'

# step 3-2 인트로 구현
# 정렬 기준 {:^숫자} = 가운데 / {:>숫자} = 오른쪽/ {:<숫자} = 왼쪽
print(Game_icon * Game_icon_max_line)
print( f'{Game_icon} {game_title:^28} {Game_icon}')
print( f'{Game_icon} {player_name:^28} {Game_icon}')
print( f'{Game_icon} {Game_version:^28} {Game_icon}')
print(Game_icon * Game_icon_max_line)

is_game_playing = True # 게임진행 플래그 (False : 게임 종료)
while is_game_playing :
    # TODO step 4-1 난수 발생, 변수명 ai_number
    # ai가 생성하는 난수의 범위를 리소스로 관리해서 외부에 적용하도록 대비
    import random
    ai_create_num_min = 1
    ai_create_num_max = 100
    ai_number = random.randint(ai_create_num_min,ai_create_num_max)
    print(f'step 4완료, AI의 생성값={ai_number}')

    # TODO step 5
    '''
    플레이어가 값을 하나 입력
    A.최초 프롬프트 제시
    "Ai가 생성한 1~100사이 중 하나를 넣어서 맞추시오"
    B.사용자 입력 -> 엔터
    C.검사
    빈값 -> 정확하게 입력하세요 -> 다시 A 부터
    정수값이 아니면 -> 정수값을 정확하게 입력하세요 -> 다시 A부터
    체크, "",isXXX() 체크
    1보다 작거나(<), 100보다 크면(>) -> 다시 A부터
    적당한 메시지 필요 (생략)
    정상
    '''
    #리소스 정리.
    player_input_prompt = f'Ai가 생성한 {ai_create_num_min}~{ai_create_num_max}\
        사이 중 하나를 넣어서 맞추시오 \n\n >'
    err_msg3 = '정수값을 입력하세요'

    try_count = 0
    while True:
        while True:
            #플레이어의 값 입력
            player_number = input(player_input_prompt).strip()
            #2. 검사
            if not player_number: #빈값 -> 정확하게 입력하세요 -> 다시 A 부터 = 문자열 일때
                print(err_msg2)
                continue
            if not player_number.isnumeric(): #정수값이 아니면 -> 정수값을 정확하게 입력하세요 -> 다시 A부터 = 문자열 일때
                print(err_msg3)
                continue
            player_number = int(player_number)
            if  (player_number<1) or (player_number>100): # 1보다 작거나(<), 100보다 크면(>) -> 다시 A부터 = 정수여야 가능하므로 변환 해줘야됨
                print(err_msg2)
                continue
            break

        #print('step 5 플레이어 입력 완료', player_number)

        # TODO step 6
        '''
        판단 (정답)
        ai값과 플레이어의 값 비교
        크다
        힌트(자율적) 제공 -> 다시 A
        작다
        힌트(자율적) 제공 -> 다시 A
        같다
        게임 클리어 -> 점수 계산
        (10-시도회수)*10
        점수 출력(형식을 자율적)
        '''
        err_msg4 = "입력된 값이 정답보다 큽니다"
        err_msg5 = "입력된 값이 정답보다 작습니다"
        msg1 = "정답입니다"

        try_count += 1 # 시도횟수 증가

        if player_number > ai_number :
            print(err_msg4)
        elif player_number < ai_number:
            print(err_msg5)
        else:
            print(msg1,f'step5,6 완료 총 점수는{(11-try_count) * 10} 입니다')
            break

    73



    # TODO step 7
    '''

    프럼프트 출력
    다시 게임을 하시겠습니까?
    yes, y, Y, YES, Yes, yEs, yeS,.. => 동의로 해석
    다시 게임으로 진행 -> STEP 4
    n, N, NO, No, no, No,..
    게임 종료
    "Bye Bye ~!"
    '''
    # step 7-1 리소스 정리
    player_input_prompt2 = '다시 게임을 진행 하시겠습니까? (y/n)'   
    msg2 = "Bye Bye ~!"
    while True: # 좋은 표현은 아니지만 여기서는 연습을 위해서 주로 사용


        player_reply = input(player_input_prompt2).strip().lower()
        if player_reply in ['yes','y'] :
            break
        elif player_reply in ['no','n'] :
            print(msg2)
            is_game_playing = False #break 밑에 있으면 실행되지 않음 break 위로 위치 조정
            break
            # 전체 게임을 탈출하려면 -> step 7 종료후
        else:
            print(err_msg)

#반복문 안에서 동일한 내용이 계속해서 발생된다면
#상수 생성(값을 초기화는 관계없다), 객체 생성(나중에 체크), (반복분 위로 위치 조정)
#속도저하가 올만한 반복적인 작업들은 위치 조정...
