import pyautogui as pag
import time
import keyboard
import threading as th

keep_going = True
def key_capture_thread():
    global keep_going
    a = keyboard.read_key()

    if a== "q":
        keep_going = False


def main():
    th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True).start()

    while keep_going:
        center = pag.locateCenterOnScreen('google_test.png')
        print(center)
        if center is not None:
            pag.click(center)
            time.sleep(0.3)

        #     center = pag.locateCenterOnScreen('done_test.png')
            
        #     if center is not None:
        #         pag.click(center)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
