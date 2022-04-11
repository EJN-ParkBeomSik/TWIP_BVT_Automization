import pyautogui as pag
import time
import keyboard
import threading as th

# 루프 강제 탈출용 'q' 버튼 누르면 탈출가능 이였으나 모든 라인마다 조건을 확인해야해서 무쓸모 왼쪽위에 마우스커서를 놓고있는게 나음.
keep_going = True
def key_capture_thread():
    global keep_going
    a = keyboard.read_key()

    if a== "q":
        keep_going = False



# 한/영 확인용 코드, 현재 동작 안함 다른 수단 찾아야함.
import ctypes
import time
from ctypes import wintypes
wintypes.ULONG_PTR = wintypes.WPARAM
hllDll = ctypes.WinDLL ("User32.dll", use_last_error=True)
VK_HANGUEL = 0x15

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

def get_hanguel_state():
    print("NOW STATE")
    print(hllDll.GetKeyState(VK_HANGUEL))
    print("0 : is EN")
    print("1 : is KR")
    print("#########################")
    return hllDll.GetKeyState(VK_HANGUEL)


def change_state():
    x = INPUT(type=1 ,ki=KEYBDINPUT(wVk=VK_HANGUEL))
    y = INPUT(type=1, ki=KEYBDINPUT(wVk=VK_HANGUEL,dwFlags=2))
    hllDll.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
    time.sleep(0.05)
    hllDll.SendInput(1, ctypes.byref(y), ctypes.sizeof(y))


#getkeystate : https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getkeystate
#sendinput : https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendinput
#code : https://gist.github.com/Aniruddha-Tapas/1627257344780e5429b10bc92eb2f52a
# get_hanguel_state()
# import sys
# sys.exit()
# #영 > 한
# if get_hanguel_state() == 0: #0 일경우 vk_key : 0x15(한글키)가 비활성화
#     change_state() #한글키 누르고(key_press) , 때기(release)


def main():
    '''
    크롬 주소창에 한영 확인 후 바탕화면 크롬아이콘 보이게 시작 -> 윈도우버튼 누르고 chrome 검색 실행으로 바꾸는게 나을듯
    '''
    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()

    while keep_going:
        time.sleep(1)

        # 바탕화면 크롬 아이콘 더블클릭
        center = pag.locateCenterOnScreen('asset/1440/chrome_desktop_icon.png')
        time.sleep(1)

        if center is not None:
            print("Found Chrome")
            pag.doubleClick(center)
            time.sleep(3)

        else:
            print("CAN'T FIND CHROME IN DESKTOP")
            break
        
        # 시크릿 탭 열기
        pag.hotkey('ctrl', 'shift', 'n')
        time.sleep(3)

        # 크롬 최대화
        pag.hotkey('alt', 'space')
        pag.hotkey('x')
        time.sleep(3)

        # 지메일 이동
        pag.typewrite('gmail.com', interval=0.1)
        pag.press('enter')
        time.sleep(5)
        
        # center = pag.locateCenterOnScreen('asset/1440/gmail_login.png')
        
        # if center is not None:
        #     pag.click(center)
            
        # 지메일 아이디 입력
        pag.typewrite('beomtest95', interval=0.1)
        time.sleep(1)
        pag.press('enter')
        time.sleep(10)

        # else:
        #     print("CAN'T FOUND LOGIN BUTTON IN GMAIL")
        #     break
        
        # 지메일 비밀번호 입력
        pag.typewrite('ejn123!@', interval=0.1)
        time.sleep(1)
        pag.press('enter')
        time.sleep(10)

        # 새 탭 열기
        pag.hotkey('ctrl', 't')
        time.sleep(1)

        # 트윕 스테이징 접속
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
                break

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
                break

        else:
            print("Found Login ID/PW Position")
            print(2.5)
        
        print(3)
        x,y_origin = center 
        y = y_origin-39 # 아이디창
        center = (x,y)
        
        pag.click(center)
        time.sleep(1)

        #한 > 영, 동작안함.
        if get_hanguel_state() == 1: #1 일경우 vk_key : 0x15(한글키)가 활성화
            change_state() #한글키 누르고(key_press) , 때기(release)

        # 아이디 입력
        pag.typewrite('beomtest95', interval=0.1)
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
        pag.hotkey('ctrl','tab')
        time.sleep(10)
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
                break
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
        pag.press('down')
        pag.press('down')
        pag.press('down')
        pag.press('down')
        pag.press('down')
        pag.press('down')
        pag.press('down')
        pag.press('down')
        pag.press('down')
        pag.press('down')
        pag.press('down')
        pag.press('down')

        # 언어에 따라 인증번호 위치 서치
        if en_flag:                
            center = pag.locateCenterOnScreen('asset/1440/find_code_en.png')
        else:
            center = pag.locateCenterOnScreen('asset/1440/find_code.png')
            
        if center is not None:
            print("Found Login code in MAail")
            print(6)
            x, y = center
            y = y + 55

            center = (x,y)
            pag.doubleClick(center)
            time.sleep(1)

        else:
            print("CAN'T FIND LOGIN CODE IN MAIL")
            print(5.9)
            break

        # 인증번호 복사
        pag.hotkey('ctrl','c')
        time.sleep(1)

        # 트위치 로그인 화면으로 탭 변경
        pag.hotkey('ctrl','tab')
        time.sleep(1)

        # 로그인 코드 입력 위치 서치
        center = pag.locateCenterOnScreen('asset/1440/login_code_input.png')
        
        if center is not None:
            print("Found typing Login code Position")
            print(7)
            pag.click(center)

            # 인증번호 붙여 넣기
            pag.hotkey('ctrl','v')
            time.sleep(10)
            
        else:
            print("CAN'T FIND THE POSITION OF TO TYPE LOGIN CODE")
            print(6.9)
            break

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
        
        # 새 시크릿 창 열기
        pag.hotkey('ctrl','shift','n')
        time.sleep(1)

        # Alert Box 오버레이 주소 입력
        pag.typewrite('https://ejn.mytwip.net/widgets/alertbox/7mMNp5qvL7', interval=0.1)
        time.sleep(1)
        pag.press('enter')
        time.sleep(5)

        # 좌로 밀착
        pag.hotkey('winleft','left')
        time.sleep(1)
        pag.hotkey('winleft')
        pag.hotkey('winleft')
        time.sleep(1)
        
        # 새 시크릿 창 열기
        pag.hotkey('ctrl','shift','n')
        time.sleep(1)

        # 후원페이지 접속
        pag.typewrite('https://ejn.mytwip.net/beomtest95', interval=0.1)
        time.sleep(1)
        pag.press('enter')
        time.sleep(5)

        # 우상 밀착
        pag.hotkey('winleft','right')
        time.sleep(1)
        pag.hotkey('winleft')
        pag.hotkey('winleft')
        time.sleep(1)
        pag.hotkey('winleft','up')
        pag.hotkey('winleft')
        pag.hotkey('winleft')
        time.sleep(1)

        if center is not None:
            print("Found Done Twitch Login button in done page")
            print(9)
            pag.click(center)
            time.sleep(10)

        else:
            print("CAN'T FINT THE DONE TWITCH LOGIN BUTTON IN DONE PAGE")
            print(8.9)
        

        # 새 시크릿 창 열기
        pag.hotkey('ctrl','shift','n')
        time.sleep(1)

        # 잔액 마이페이지 접속
        pag.typewrite('https://ejn.mytwip.net/member/mypage', interval=0.1)
        time.sleep(1)
        pag.press('enter')
        time.sleep(5)

        # 우하 밀착
        pag.hotkey('winleft','right')
        time.sleep(1)
        pag.hotkey('winleft')
        pag.hotkey('winleft')
        time.sleep(1)
        pag.hotkey('winleft','down')
        time.sleep(1)
        pag.hotkey('winleft')
        pag.hotkey('winleft')
        time.sleep(1)

        # 후원 페이지 트위치 로그인 버튼
        center = pag.locateCenterOnScreen('asset/1440/done_twitch_login.png')

        if center is not None:
            print("Found Done Twitch Login button in done page")
            print(9)
            pag.click(center)
            time.sleep(10)

        else:
            print("CAN'T FINT THE DONE TWITCH LOGIN BUTTON IN DONE PAGE")
            print(8.9)
        

if __name__ == "__main__":
    main()
