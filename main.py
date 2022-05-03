from login import login
from window_setting import window_setting
from real_done import donation
from mission_done import mission_done
import time

def main():
    login()
    window_setting()
    donation()
    
    before_clipboard_data = -1

    for i in range(2):
        before_clipboard_data = mission_done(before_clipboard_data)
        print("please wait 3minute")

        # 미션 후원 최소 등록 시간 기다릭
        time.sleep(180)


if __name__ == "__main__":
    main()