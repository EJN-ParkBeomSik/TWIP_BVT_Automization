import pyautogui as pag
import time
import keyboard
import threading as th
import win32clipboard

keep_going = True

def key_capture_thread():
    global keep_going
    a = keyboard.read_key()

    if a== "q":
        keep_going = False

def donation():
    done_price = 2000
    before_clipboard_data = -1
    count = 0
    asset_path = "asset/1440/"

    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()

    while keep_going:
        # 후원 완료 창이 있을 경우 새로고침 필요
        center = pag.locateCenterOnScreen(asset_path + 'done_thx_2.png')
        print("step 0")
        if center is not None:
            pag.click(center)
            time.sleep(2)

            pag.press('f5')
            time.sleep(5)

        # 후원 금액 변경
        center = pag.locateCenterOnScreen(asset_path + 'donation_price.png')
        print("step 0.5")
        
        if center is not None:
            print("Found Donation Price Setting")
            pag.doubleClick(center)
            time.sleep(0.3)

            pag.typewrite('%s'%done_price, interval=0.1)

        else:
            print("Try to find another price image")
            # 후원 금액 변경2
            center = pag.locateCenterOnScreen(asset_path + 'donation_price_2.png')
            print("step 0.5")
            
            if center is not None:
                print("Found Donation Price Setting_2")
                pag.doubleClick(center)
                time.sleep(0.3)

                pag.typewrite('%s'%done_price, interval=0.1)

            else:
                print("CAN'T FIND DONATION PRICE SETTING")
                break


        # 후원 메세지 입력
        center = pag.locateCenterOnScreen(asset_path + 'message_click_2.png')
        print("step 1")

        if center is not None:
            print("Found Message Window")
            pag.click(center)
            time.sleep(0.3)

            pag.typewrite('Hello world!', interval=0.1)

        else:
            print("CAN'T FIND MESSAGE WINDOW")
            break

        # 후원 버튼 찾기
        center = pag.locateCenterOnScreen(asset_path + 'real_done_buttoon.png')        
        print("step 2")
        time.sleep(2)

        if center is not None:
            print("Found Donation Button")
            pag.click(center)
            time.sleep(7)

        else:
            print("CAN'T FIND DONATION BUTTON")
            break
        
        # Alert Box 후원 결과 찾기
        center = pag.locateCenterOnScreen(asset_path + 'done_result.png')        
        print("step 3")
        
        if center is None:
            print("CAN'T FIND DONATION RESULT")
            print()
            print("#################")
            tm = time.localtime()
            time_msg = time.strftime('%Y-%m-%d %I:%M:%S %p', tm)
            print(time_msg)                    
            print("Failed donation!!")
            print("#################")

        else:
            print("Found Donation Result")
            print()
            tm = time.localtime()
            time_msg = time.strftime('%Y-%m-%d %I:%M:%S %p', tm)

            print(time_msg)                    
            print("Successed donation!!")

        time.sleep(5)

        # 현재 잔액 찾기
        center = pag.locateCenterOnScreen(asset_path + 'janek.png')        
        print("step 4")

        if center is not None:
            print("Found Now Money")
            print("step 5")
            
            pag.click(center)
            time.sleep(2)
            pag.press('f5')
            time.sleep(5)

            x,y = center
            x = x + 35
            center = (x,y)

            pag.doubleClick(center)
            time.sleep(2)

            # 현재 잔액 복사
            pag.hotkey('ctrl','c')
            time.sleep(2)

            # 복사된 잔액을 변수로 받음
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
                # 만약 첫 루프면 기존 잔액이 없으므로 스킵
                if count == 0:
                    print("First Loop. Cant't judge Cash")

                else:
                    print("Cash is bad")

            print()
            
            # 현재 잔액을 기존 잔액으로 업데이트
            before_clipboard_data = clipboard_number

        else:
            print("CAN'T FIND NOW MONEY")
            break

        time.sleep(5)
        count += 1

if __name__ == "__main__":
    donation()
