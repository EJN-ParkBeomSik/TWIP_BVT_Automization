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
    done_price = 1000
    before_clipboard_data = -1
    count = 0
    asset_path = "asset/1440/"

    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()

    while keep_going:
        center = pag.locateCenterOnScreen(asset_path + 'done_thx_2.png')
        print("step 0")
        if center is not None:
            pag.click(center)
            time.sleep(2)

            pag.press('f5')
            time.sleep(5)
        
        center = pag.locateCenterOnScreen(asset_path + 'message_click_2.png')
        print("step 1")
        # 도네 가격 변경 추가필요
        if center is not None:
            pag.click(center)
            time.sleep(0.3)

            pag.typewrite('Hello world!', interval=0.1)
            center = pag.locateCenterOnScreen(asset_path + 'real_done_buttoon.png')        
            print("step 2")
            time.sleep(2)

            if center is not None:
                pag.click(center)
                time.sleep(7)

                center = pag.locateCenterOnScreen(asset_path + 'done_result.png')        
                print("step 3")
                if center is None:
                    print()
                    print("#################")
                    tm = time.localtime()
                    time_msg = time.strftime('%Y-%m-%d %I:%M:%S %p', tm)
                    print(time_msg)                    
                    print("Failed donation!!")
                    print("#################")

                if center is not None:
                    print()
                    tm = time.localtime()
                    time_msg = time.strftime('%Y-%m-%d %I:%M:%S %p', tm)

                    print(time_msg)                    
                    print("Successed donation!!")

                time.sleep(5)

                center = pag.locateCenterOnScreen(asset_path + 'janek.png')        
                print("step 4")

                if center is not None:
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

                    pag.hotkey('ctrl','c')
                    time.sleep(2)

                    win32clipboard.OpenClipboard()
                    clipboard_data = win32clipboard.GetClipboardData()
                    win32clipboard.CloseClipboard()
                    
                    clipboard_data_list = clipboard_data.split(",")
                    clipboard_number = int("".join(clipboard_data_list))
                    
                    print()
                    print("BEFORE Janek : ", before_clipboard_data)
                    print("NOW Janek : ", clipboard_data)
                    print()

                    if before_clipboard_data - clipboard_number == done_price:
                        print("Janek is good")
                    else:
                        if count == 0:
                            print("First Loop. Cant't judge Janek")

                        else:
                            print("Janek is bad")

                    print()

                    before_clipboard_data = clipboard_number

        time.sleep(5)
        count += 1

if __name__ == "__main__":
    donation()
