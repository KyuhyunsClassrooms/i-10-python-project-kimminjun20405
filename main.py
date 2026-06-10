# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 
# 프로젝트 주제: 
import random
import time

def show_menu():
    while True:
        print("\n=== ⚡ 콘솔 서바이벌 리듬 게임 ⚡ ===")
        print("1. 레벨 1 (시간: 2.0초 | 목숨: 5개 | 난이도: ★☆☆)")
        print("2. 레벨 2 (시간: 1.2초 | 목숨: 3개 | 난이도: ★★☆)")
        print("3. 레벨 3 (시간: 0.8초 | 목숨: 1개 | 난이도: ★★★)")
        print("4. 게임 종료")
        print("=====================================")
        
        choice = input("도전할 레벨의 번호를 입력하세요: ")
        
        if choice == "1":
            print("\n🎮 [레벨 1] 게임을 시작합니다. 차근차근 연습해 보세요!")
            return 1
        elif choice == "2":
            print("\n🔥 [레벨 2] 게임을 시작합니다. 집중력이 필요합니다!")
            return 2
        elif choice == "3":
            print("\n💀 [레벨 3] HARDCORE MODE! 단 한 번의 실수도 용납되지 않습니다!")
            return 3
        elif choice == "4":
            print("\n👋 게임을 종료합니다. 다음에 또 도전해 주세요!")
            return 0
        else:
            print("\n❌ 잘못된 입력입니다. 1, 2, 3, 4 중에서 올바른 번호를 골라주세요.")


# --- 위에 작성한 show_menu() 함수가 있다고 가정합니다 ---

# 메인 실행부
selected_level = show_menu()

if selected_level == 1:
    limit_time = 2.0
    initial_life = 5
    print(f"[시스템] 제한 시간 {limit_time}초, 목숨 {initial_life}개로 게임을 세팅합니다...")
    # (다음 단계에서 여기에 play_rhythm_game("레벨 1", limit_time, initial_life)를 호출할 거예요!)

elif selected_level == 2:
    limit_time = 1.2
    initial_life = 3
    print(f"[시스템] 제한 시간 {limit_time}초, 목숨 {initial_life}개로 게임을 세팅합니다...")

elif selected_level == 3:
    limit_time = 0.8
    initial_life = 1
    print(f"[시스템] 제한 시간 {limit_time}초, 목숨 {initial_life}개로 초고난도 게임을 세팅합니다... ⚡")