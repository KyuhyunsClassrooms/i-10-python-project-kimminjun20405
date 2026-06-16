# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20405 김민준
# 프로젝트 주제: 리듬게임
import random
import time

# ==========================================
# 1. 최종 등급 판정 함수 (가장 먼저 읽어야 함)
# ==========================================
def calculate_grade(score):
    if score >= 90:
        return "🏆 A등급 (리듬의 신)"
    elif score >= 80:
        return "✨ B등급 (실력자)"
    elif score >= 70:
        return "👍 C등급 (노력파)"
    elif score >= 50:
        return "👍 D등급 (초보자)"
    else:
        return "🌱 F등급 (재도전 필요)"


# ==========================================
# 2. 시작 메뉴 화면 함수
# ==========================================
def show_menu():
    while True:
        print("\n=== ⚡ 콘솔 서바이벌 리듬 게임 ⚡ ===")
        print("1. 레벨 1 (시간: 1.9초 | 목숨: 3개 | 난이도: ★☆☆)")
        print("2. 레벨 2 (시간: 1.3초 | 목숨: 2개 | 난이도: ★★☆)")
        print("3. 레벨 3 (시간: 0.9초 | 목숨: 1개 | 난이도: ★★★)")
        print("4. 게임 종료")
        print("=====================================")
        
        choice = input("도전할 레벨의 번호를 입력하세요: ")
        
        if choice == "1":
            print("\n🎮 [레벨 1] 게임 세팅 중...")
            return 1
        elif choice == "2":
            print("\n🔥 [레벨 2] 게임 세팅 중...")
            return 2
        elif choice == "3":
            print("\n💀 [레벨 3] HARDCORE MODE 세팅 중... ⚡")
            return 3
        elif choice == "4":
            print("\n👋 게임을 종료합니다. 다음에 또 도전해 주세요!")
            return 0
        else:
            print("\n❌ 잘못된 입력입니다. 1, 2, 3, 4 중에서 올바른 번호를 골라주세요.")


# ==========================================
# 3. 핵심 게임 플레이 함수
# ==========================================
def play_rhythm_game(level_name, limit_time, initial_life):
    # [수정 디테일] 현재 노트를 12개로 설정했으므로 안내 문구도 12개로 수정했어요!
    print(f"\n--- 🎮 {level_name} 게임 시작! ---")
    print(f"노트는 총 12개! 제한시간: {limit_time}초 | 시작 목숨: {initial_life}개")
    print("---------------------------------")
    
    # 게임 시작 전 3, 2, 1 카운트다운 효과
    print("게임을 시작합니다...")
    for count in range(3, 0, -1): # 3부터 1까지 1씩 감소
        print(f"⏱️ {count}...")
        time.sleep(1) # 1초 동안 멈춤
    print("🚀 START!!")
    print("---------------------------------")
    
    total_score = 0
    life = initial_life # 현재 목숨을 시작 목숨으로 세팅
    
    # [2번 방식 적용] 셔플 방식을 위한 키 풀(Pool) 바구니 준비
    game_notes = []
    current_pool = []
    
    for i in range(1, 26): # 총 12개의 노트 생성
        # 만약 바구니가 비어있다면, QWER을 새로 넣고 무작위로 뒤섞기
        if not current_pool:
            current_pool = ["Q", "W", "E", "R"]
            random.shuffle(current_pool) # 리스트 요소를 무작위로 섞어줌
            
        # 바구니에서 맨 뒤에 있는 키를 하나 쏙 빼서 정답 키로 사용 (4노트 연속 중복 방지!)
        random_key = current_pool.pop()
        game_notes.append([i, random_key, 4])
        
    # for문으로 2차원 리스트 탐색
    for note in game_notes:
        # 게임 도중 목숨을 모두 잃으면 즉시 반복문 탈출
        if life <= 0:
            print("\n💀 목숨을 모두 잃었습니다... GAME OVER 💀")
            break
            
        note_num = note[0]
        correct_key = note[1]
        points = note[2]
        
        print(f"\n🎵 [노트 {note_num}] 현재 목숨: {'❤️' * life} | [{correct_key}] 키를 누르세요!")
        
        start_time = time.time()
        user_input = input("입력: ")
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        
        # 제한 시간을 초과한 경우
        if elapsed_time > limit_time:
            print(f"⏱️ 시간 초과! ({elapsed_time:.2f}초 걸림) 목숨 -1, 점수 -5")
            life = life - 1
            total_score = total_score - 5
            continue
            
        # 시간 안에 올바른 키를 입력한 경우
        if user_input.upper() == correct_key:
            print(f"✨ Perfect! ({elapsed_time:.2f}초 만에 성공! +{points}점)")
            total_score = total_score + points
        # 틀린 키를 입력한 경우
        else:
            print(f"❌ 틀린 키를 입력했습니다! 목숨 -1")
            life = life - 1
            
    # 게임 종료 후 결과 및 등급 출력
    print("\n=================================")
    print(f"🎉 게임 종료! 최종 점수: {total_score}점")
    
    # 최종 등급 판정 함수 호출
    grade = calculate_grade(total_score)
    print(f"🏅 최종 등급: {grade}")
    print("=================================")
    
    return total_score


# ==================================================
# 4. 메인 서브 실행부 (★반드시 코드의 가장 마지막, 맨 아래에 위치해야 함★)
# ==================================================
while True:
    selected_level = show_menu()
    
    # 사용자가 4번(종료)을 누르면 무한 루프 탈출!
    if selected_level == 0:
        break
        
    # レ벨별 변수 세팅
    if selected_level == 1:
        limit_time = 1.9
        initial_life = 3
        level_name = "레벨 1"
    elif selected_level == 2:
        limit_time = 1.3
        initial_life = 2
        level_name = "레벨 2"
    elif selected_level == 3:
        limit_time = 0.9
        initial_life = 1
        level_name = "레벨 3"
        
    print(f"[시스템] 제한 시간 {limit_time}초, 목숨 {initial_life}개로 게임을 세팅합니다...")
    
    # 게임 실행
    final_score = play_rhythm_game(level_name, limit_time, initial_life)