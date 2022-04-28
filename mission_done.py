import pyautogui as pag
import time
import keyboard
import threading as th
import win32clipboard

def mission_done():
    print("#######################################")
    print("#######################################")
    print("############## MISSION ################")
    print("#######################################")
    print("#######################################")
    
    done_price = 5000
    before_clipboard_data = -1
    count = 0
    asset_path = "asset/1440/"

    # 후원 완료 창을 찾아 새로고침
    center = pag.locateCenterOnScreen(asset_path + 'done_thx_2.png')
    print("step 0")

    if center is not None:
        pag.click(center)
        time.sleep(2)

        print("refresh the page")
        pag.press('f5')
        time.sleep(5)

    else:
        # 새로고침 필요
        center = pag.locateCenterOnScreen(asset_path + 'mission_after_done_page_click.png')
        print("step 0")

        if center is not None:
            pag.click(center)
            time.sleep(2)

            print("refresh the page")
            pag.press('f5')
            time.sleep(5)
        
        else:
            print("can't refresh the page")
            raise
            
    # 미션 페이지 진입
    center = pag.locateCenterOnScreen(asset_path + 'mission.png')
    print("step 1")

    if center is not None:
        print("Found mission button")
        pag.click(center)
        time.sleep(1)

    else:
        print("can't find mission button")
        raise

    # 미션 내용 입력
    center = pag.locateCenterOnScreen(asset_path + 'mission_neyong.png')
    print("step 2")

    if center is not None:
        print("Found mission neyong")
        pag.click(center)
        time.sleep(1)

        print("type message")
        pag.typewrite('Hello mission!', interval=0.1)

    else:
        print("can't find mission neyong")
        raise

    # 미션 후원 가격
    center = pag.locateCenterOnScreen(asset_path + 'mission_price.png')
    print("step 3")

    if center is not None:
        print("Found mission price")
        pag.click(center)
        time.sleep(1)

        print("type precie")
        pag.typewrite('5000', interval=0.1)

    else:
        print("can't find mission price")
        raise

    # 미션 제한 시간
    center = pag.locateCenterOnScreen(asset_path + 'time_limit.png')
    print("step 4")

    if center is not None:
        print("Found the limit time")
        pag.click(center)
        time.sleep(1)

    else:
        print("can't find mission price")
        raise

    # 미션 제한 시간 3시간 클릭
    center = pag.locateCenterOnScreen(asset_path + 'done_3.png')
    print("step 5")

    if center is not None:
        print("Found 3 hour")
        pag.click(center)
        time.sleep(1)

        print("click minute")
        x, y = center
        x = x + 70
        
        pag.click((x,y))
        time.sleep(1)

    else:
        print("can't find 3 hour")
        raise

    # 미션 등록하기
    center = pag.locateCenterOnScreen(asset_path + 'mission_up.png')
    print("step 6")

    if center is not None:
        print("register the mission")
        pag.click(center)
        time.sleep(10)

    else:
        print("can't find register button")
        raise
    
    # 미션 최종 체크하여 등록하기
    center = pag.locateCenterOnScreen(asset_path + 'mission_register_check.png')
    print("step 7")

    if center is not None:
        print("final check the mission")
        pag.click(center)
        time.sleep(10)

    else:
        print("can't find check button")
        raise

    # 현재 잔액 찾기
    center = pag.locateCenterOnScreen(asset_path + 'janek.png')        
    print("step 4")

    if center is not None:
        print("Found Now Money")
        print("step 5")
        
        pag.click(center)
        time.sleep(2)
        
        print("refresh")
        pag.press('f5')
        time.sleep(5)

        x,y = center
        x = x + 35
        center = (x,y)

        print("double click money")
        pag.doubleClick(center)
        time.sleep(2)

        # 현재 잔액 복사
        print("copy the mnoney")
        pag.hotkey('ctrl','c')
        time.sleep(2)

        # 복사된 잔액을 변수로 받음        
        print("get clipboard")
        win32clipboard.OpenClipboard()
        clipboard_data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        
        # 복사된 잔액을 정수로 변환
        clipboard_data_list = clipboard_data.split(",")
        clipboard_number = int("".join(clipboard_data_list))
        
        # 복사된 잔액과, 기존 루프에서 남은 잔액을 출력
        print()
        print("BEFORE Cash : ", before_clipboard_data)
        print("NOW Cash : ", clipboard_data)
        print()

        # 복사된 잔액과 기존 잔액의 차이가 후원 캐시와 같은지 체크
        if before_clipboard_data - clipboard_number == done_price:
            print("Cash is good")

        else:
            # # 만약 첫 루프면 기존 잔액이 없으므로 스킵
            # if count == 0:
            #     print("First Loop. Cant't judge Cash")

            # else:
            #     print("Cash is bad")
            print("Cash is bad")

        print()
        
        # 현재 잔액을 기존 잔액으로 업데이트
        before_clipboard_data = clipboard_number

    else:
        print("CAN'T FIND NOW MONEY")
        raise

    time.sleep(5)


if __name__ == "__main__":
    mission_done()

    