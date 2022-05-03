import pyautogui as pag
import time

def login():
    
    print("#######################################")
    print("#######################################")
    print("################ LOGIN ################")
    print("#######################################")
    print("#######################################")
    time.sleep(1)

    # 시작 -> 크롬 열기
    print("press windows key")
    pag.hotkey('winleft')
    time.sleep(1)

    print("type chrome")
    pag.typewrite('chrome', interval=0.1)
    pag.press('enter')
    time.sleep(5)
    
    # 시크릿 탭 열기
    print("open secret tab")
    pag.hotkey('ctrl', 'shift', 'n')
    time.sleep(3)

    # 크롬 최대화
    print("expand chrome")
    pag.hotkey('alt', 'space')
    pag.hotkey('x')
    time.sleep(3)

    # 지메일 이동
    print("type gmail")
    pag.typewrite('gmail.com', interval=0.1)
    pag.press('enter')
    time.sleep(5)
    
    # center = pag.locateCenterOnScreen('asset/1440/gmail_login.png')
    
    # if center is not None:
    #     pag.click(center)
        
    # 지메일 아이디 입력
    print("type gmail id")
    pag.typewrite('beomtest95', interval=0.1)
    time.sleep(1)
    pag.press('enter')
    time.sleep(10)

    # else:
    #     print("CAN'T FOUND LOGIN BUTTON IN GMAIL")
    #     break
    
    # 지메일 비밀번호 입력
    print("type gmail pw")
    pag.typewrite('ejn123!@', interval=0.1)
    time.sleep(1)
    pag.press('enter')
    time.sleep(10)

    # 새 탭 열기
    print("open new tab")
    pag.hotkey('ctrl', 't')
    time.sleep(1)

    # 트윕 스테이징 접속
    print("type twip page")
    pag.typewrite('https://ejn.mytwip.net/', interval=0.1)
    time.sleep(1)
    pag.press('enter')
    time.sleep(10)

    # 트윕 로그인
    center_origin = pag.locateCenterOnScreen('asset/1440/streamer_login.png')

    if center_origin is None:
        print("FIND ANOTHER STREAMER_LOGIN IMG")
        center_origin = pag.locateCenterOnScreen('asset/1440/streamer_login_2.png')

        if center_origin is not None:
            print("Found another one")
        
            pag.click(center_origin)
            time.sleep(1)

            # 트윕 재로그인하세요 창 에러 방지용
            center = pag.locateCenterOnScreen('asset/1440/streamer_login_2.png')

            if center is not None:
                pag.click(center)
                time.sleep(5)
            else:
                pag.click(center_origin)
                time.sleep(5)
        
        else:
            print("CAN'T FIND LOGIN BUTTON IN TWIP")
            raise

    else:
        print(1)
        pag.click(center_origin)
        time.sleep(1)

        # 트윕 재로그인하세요 창 에러 방지용
        center = pag.locateCenterOnScreen('asset/1440/streamer_login.png')
    
        if center is not None:
            pag.click(center)
            time.sleep(5)
        else:
            pag.click(center_origin)
            time.sleep(5)

    # 트위치 로그인창 확인
    center = pag.locateCenterOnScreen('asset/1440/not_login2.png')

    if center is None:
        print("FIND ANOTHER LOGIN ID/PW POSITION")

        # 트위치 로그인창 키보드 커서 위치 버그 방지용        
        center = pag.locateCenterOnScreen('asset/1440/not_login.png')

        if center is not None:
            print("Found Another One")
            print(2)
        
        else:
            print("CAN'T FIND LOGIN ID/PW POSITION")
            print(1.9)
            raise

    else:
        print("Found Login ID/PW Position")
        print(2.5)
    
    print(3)
    x,y_origin = center 
    y = y_origin-39 # 아이디창
    center = (x,y)
    
    pag.click(center)
    time.sleep(1)

    # #한 > 영, 동작안함.
    # if get_hanguel_state() == 1: #1 일경우 vk_key : 0x15(한글키)가 활성화
    #     change_state() #한글키 누르고(key_press) , 때기(release)

    # 트위치 아이디 입력
    print("type id")
    pag.typewrite('beomtest95_2', interval=0.1)
    time.sleep(1)

    y = y_origin -80 # 자동로그인 창 버그 해결용 클릭
    center = (x,y)
    pag.click(center)
    time.sleep(1)

    y = y_origin + 40 # 비번창
    center = (x,y)
    pag.click(center)
    time.sleep(1)  

    # 비번 입력
    print("type pw")
    pag.typewrite('ejn123!@ejn123!@', interval=0.1)
    time.sleep(1)

    pag.press('enter')
    time.sleep(10)

    # # 트위치 로그인 버튼
    # center = pag.locateCenterOnScreen('asset/1440/twitch_login.png')
    # time.sleep(1)

    # if center is not None:
    #     print(3)
    #     pag.click(center)
    #     time.sleep(10)
        
    # else:
    #     print(2.9)
    #     break

    print(4)

    # 브라우저 탭 변경
    print("add new tab")
    pag.hotkey('ctrl','tab')
    time.sleep(10)
    print("refresh")
    pag.press('f5')
    time.sleep(10)
        
    en_flag = False

    # 지메일 로그인 인증메일 서치
    center = pag.locateCenterOnScreen('asset/1440/login_mail.png')

    if center is None:
        print("CAN'T FIND LOGIN MAIL BY KR, TRY TO SEARCH EN")
        # center = pag.locateCenterOnScreen('asset/1440/login_mail2.png')

        # if center is None:

        # 메일이 영어로 왔을 가능성 체크
        en_flag = True

        # 영어 인증 메일 서치
        center = pag.locateCenterOnScreen('asset/1440/login_mail_en.png')

            # if center is None:
            #     print("5.5.en")
                # center = pag.locateCenterOnScreen('asset/1440/login_mail2_en.png')
                
        if center is not None:
            print("Found EN Login Mail")
            print("5.6.en")

        else:
            print("CAN'T FIND LOGIN MAIL BY EN, KR.")
            print(4.95)
            raise
            # else:
            #     print(4.9)
            #     break
        # else:
        #     print(5.6)
    
    else:
        print("Found KR Login Mail")
        print(5)

    pag.click(center)
    time.sleep(5)

    # 인증 메일이 많이 와서 인증번호가 안나올 가능성 방지
    print("press down")

    for temp_num in range(12):
        pag.press('down')

    # 언어에 따라 인증번호 위치 서치
    if en_flag:                
        center = pag.locateCenterOnScreen('asset/1440/find_code_en.png')
    else:
        center = pag.locateCenterOnScreen('asset/1440/find_code.png')
        
    if center is not None:
        print("Found Login code in Mail")
        print(6)
        x, y = center
        y = y + 55

        center = (x,y)
        pag.doubleClick(center)
        time.sleep(1)

    else:
        print("CAN'T FIND LOGIN CODE IN MAIL")
        print(5.9)
        raise

    # 인증번호 복사
    print("copy the number")
    pag.hotkey('ctrl','c')
    time.sleep(1)

    # 트위치 로그인 화면으로 탭 변경
    print("change the tab")
    pag.hotkey('ctrl','tab')
    time.sleep(1)

    # 로그인 코드 입력 위치 서치
    center = pag.locateCenterOnScreen('asset/1440/login_code_input.png')
    
    if center is not None:
        print("Found typing Login code Position")
        print(7)
        pag.click(center)

        # 인증번호 붙여 넣기
        print("paste the number")
        pag.hotkey('ctrl','v')
        time.sleep(10)
        
    else:
        print("CAN'T FIND THE POSITION OF TO TYPE LOGIN CODE")
        print(6.9)
        raise

    # 로그인 완료

    # 대시보드 튜토리얼 스킵버튼
    center = pag.locateCenterOnScreen('asset/1440/dashboard_skip.png')

    if center is not None:
        print("Found skip button in dashboard page")
        print(8)
        pag.click(center)
        time.sleep(1)

    else:
        print("CAN'T FINT THE SKIP BUTTON IN DASHBOARD PAGE")
        print(7.9)
        

if __name__ == "__main__":
    login()
