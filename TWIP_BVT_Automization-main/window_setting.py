import pyautogui as pag
import time


def window_setting():
    
    print("#######################################")
    print("#######################################")
    print("########### window_setting ############")
    print("#######################################")
    print("#######################################")
    time.sleep(1)

    # 새 시크릿 창 열기
    print("open ney secret window")
    pag.hotkey('ctrl','shift','n')
    time.sleep(1)

    # 후원페이지 접속
    print("open donation page")
    pag.typewrite('https://ejn.mytwip.net/beomtest95_2', interval=0.1)
    time.sleep(1)
    pag.press('enter')
    time.sleep(5)

    # 좌로 밀착
    print("set to left")
    pag.hotkey('winleft','left')
    time.sleep(1)
    pag.hotkey('winleft')
    pag.hotkey('winleft')
    time.sleep(15)

    # 후원 페이지 트위치 로그인 버튼
    center = pag.locateCenterOnScreen('asset/1440/done_twitch_login.png')

    if center is not None:
        print("Found Done Twitch Login button in done page")
        print(9)
        pag.click(center)
        time.sleep(15)

    else:
        print("CAN'T FINT THE DONE TWITCH LOGIN BUTTON IN DONE PAGE")
        print(8.9)

    # 새 시크릿 창 열기
    print("new secret window")
    pag.hotkey('ctrl','shift','n')
    time.sleep(2)

    # Alert Box 오버레이 주소 입력
    print("open alert box overay")
    # pag.typewrite('https://ejn.mytwip.net/widgets/alertbox/7mMNp5qvL7', interval=0.1) #beomtest95
    pag.typewrite('https://ejn.mytwip.net/widgets/alertbox/KbzvAPER7g', interval=0.1) #beomtest95_2
    time.sleep(2)
    pag.press('enter')
    time.sleep(6)

    # 우상 밀착
    print("set to right up")
    pag.hotkey('winleft','right')
    time.sleep(2)
    pag.hotkey('winleft')
    pag.hotkey('winleft')
    time.sleep(2)
    pag.hotkey('winleft','up')
    pag.hotkey('winleft')
    pag.hotkey('winleft')
    time.sleep(2)

    # 새 시크릿 창 열기
    print("open new secret window")
    pag.hotkey('ctrl','shift','n')
    time.sleep(2)

    # 잔액 마이페이지 접속
    print("type mypage")
    pag.typewrite('https://ejn.mytwip.net/member/mypage', interval=0.1)
    time.sleep(2)
    pag.press('enter')
    time.sleep(6)

    # 우하 밀착
    print("set right down")
    pag.hotkey('winleft','right')
    time.sleep(2)
    pag.hotkey('winleft')
    pag.hotkey('winleft')
    time.sleep(2)
    pag.hotkey('winleft','down')
    time.sleep(2)
    pag.hotkey('winleft')
    pag.hotkey('winleft')
    time.sleep(2)
    

if __name__ == "__main__":
    window_setting()
