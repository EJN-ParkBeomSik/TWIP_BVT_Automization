# TWIP_BVT_Automization
TWIP 기본기능 테스트 자동화 with pyautogui

# Requirements
    python 3.6 이상
    PyAutoGUI 0.9.53
    keyboard 0.13.5

# Installation
    pip install pyautogui 
    pip install keyboard
    git clone https://github.com/EJN-ParkBeomSik/TWIP_BVT_Automization
    
# 크롬 시작 및 로그인, 윈도우 설정, 메시지 후원, 미션 후원
    이미지를 자신의 컴퓨터 상황에 맞게 설정한다. (asset 에 있는 이미지를 새로 캡쳐하여 저장. default : 1440p 기준)
    크롬 브라우저 주소창에서 키보드 입력의 한/영 상태가 영어인지 확인한다.
    python main.py

# 크롬 시작 및 로그인
    크롬 브라우저 주소창에서 키보드 입력의 한/영 상태가 영어인지 확인한다.
    python login.py
# 윈도우 설정
    크롬 시작 및 로그인이 진행되었다면,
    python window_setting.py
# 메시지 후원
    윈도우 설정이 완료되었다면,
    python real_done.py
# 미션 후원
    윈도우 설정이 완료되었다면,
    python mission_done.py
