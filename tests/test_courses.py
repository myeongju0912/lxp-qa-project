
from selenium.webdriver.common.by import By
import time
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_and_open_classrooms(driver, base_url):
    print("\n=== 테스트 시작 ===")

    #TC-CRS-001
    driver.get(f"{base_url}/classrooms/")
    time.sleep(2)
    
    if "accounts.elice.io" in driver.current_url or "login" in driver.current_url:

    #TC-CRS-002
        login = LoginPage(driver)
        login.fill_email("jellyfish09@naver.com")
        login.fill_password("Ff0rever@!")
        time.sleep(1)
        login.submit()

        print("로그인 버튼 클릭 완료")

    # qatrack 도메인으로 돌아올 때까지 대기
    WebDriverWait(driver, 20).until(EC.url_contains("qatrack.elice.io"))

    # my 페이지로 이동 확인
    WebDriverWait(driver, 20).until(
    lambda d: "/my" in d.current_url or "/classrooms" in d.current_url)
    print("로그인 성공 → /my 페이지 진입 확인")

    # classrooms 이동
    driver.get(f"{base_url}/classrooms/")
    WebDriverWait(driver, 15).until(EC.url_contains("/classrooms"))

    print("classrooms 페이지 진입 성공", driver.current_url)

    assert "/my" in driver.current_url or "/classrooms" in driver.current_url
    
    #TC-CRS-003 
    third_class = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[.//span[text()='3기']]"))
    )
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", third_class)
    time.sleep(0.5)
    third_class.click()
    
    print("\n🏃🏻‍➡️ 3기 코스 클릭 성공")
    
    #TC-CRS-004
    courses_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//a[.//p[text()='학습 과목']]"))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", courses_btn)
    time.sleep(0.5)
    courses_btn.click()

    print("\n 📖 학습 과목 메뉴 클릭 성공")
    
    
    #TC-CRS-006
    print("\n 📖 학습 과목 페이지로 들어왔는지 확인")

    title = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//h4[text()='학습 과목']"))
    )

    assert title.text == "학습 과목"
    print("\n 📖 학습 과목 페이지 진입 완료")
    time.sleep(5)    
    
    # ⬇️ 스크롤 한 번 내리기
    # driver.execute_script("window.scrollBy(0, 800)")
    # time.sleep(2)

    #TC-CRS-005
    scroll_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            "main div.MuiContainer-root > div.MuiStack-root"
        ))
    )

    driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight",
        scroll_box
    )
    time.sleep(1)
    
    print("\n🔍 CH12 카드 찾는 중...")

    ch12 = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((
            By.XPATH, "//p[contains(text(),'[CH12]') and contains(text(),'고급 스크립트')]"
        ))
    )

    # 카드가 화면 중앙에 오도록 스크롤
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", ch12)
    time.sleep(0.5)

    # 클릭
    ch12.click()

    print("\n🚀 [CH12] 고급 스크립트 강의 진입 성공")
    time.sleep(5)
    
    
    
    #TC-CRS-006
        # ===== 학습맵 클릭 =====
    print("\n🧠 학습맵 클릭 시도")

    learning_map_tab = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., '학습맵')]]"))
    )
    learning_map_tab.click()

    # 학습맵이 열렸는지 확인 (마인드맵 컨테이너)
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'react-draggable')]"))
    )

    time.sleep(1)
    
    print("✅ 학습맵 화면 표시 확인")


    # ===== 학습목차 클릭 =====
    print("\n📚 학습목차 클릭 시도")

    curriculum_tab = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//text()[contains(., '학습 목차')]]"))
    )
    curriculum_tab.click()


    # ===== 학습목차 페이지 로딩 완료 검증 (핵심) =====
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//h6[contains(text(),'01') and contains(text(),'자동화')]"
        ))
    )

    print("✅ 학습목차 클릭 성공")
    time.sleep(3)
        
    # # ============================
    # # 📂 현재 선택된 폴더 (01번)
    # # ============================

    # folder_button = WebDriverWait(driver, 15).until(
    #     EC.presence_of_element_located((
    #         By.XPATH,
    #         "//div[contains(@class,'MuiListItemButton-root') and contains(@class,'Mui-selected')]"
    #     ))
    # )

    # print("📌 현재 선택된 폴더 row 찾음")

    #TC-CRS-007
    #강의자료 클릭
    lecture_material = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//ul[contains(@class,'MuiList-root')]//p[contains(text(),'[강의자료]')]"
        ))
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        lecture_material
    )
    time.sleep(0.5)

    lecture_material.click()
    print("✅ 왼쪽 학습목차의 강의 자료 클릭 성공")

    # 페이지 이동 검증
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH, "//iframe | //embed | //object"
        ))
    )
    print("📄 강의 자료 페이지 진입 확인")
    time.sleep(3)
    
    # ===== 학습 종료 버튼 클릭 =====
    print("🛑 학습 종료 버튼 클릭 시도")

    end_learning_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH, "//a[normalize-space(text())='학습 종료']"
        ))
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        end_learning_btn
    )
    time.sleep(0.5)

    end_learning_btn.click()
    print("✅ 학습 종료 버튼 클릭 성공")

    # ===== 결과 검증 =====
    WebDriverWait(driver, 10).until(
        EC.url_contains("/classrooms")
    )
    print("🏁 학습 종료 후 페이지 이동 확인")
    time.sleep(3)
    
    
    print("📝 퀴즈 항목 클릭 시도")

    quiz_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//ul[contains(@class,'MuiList-root')]//p[contains(text(),'[퀴즈')]"
        ))
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        quiz_item
    )
    time.sleep(0.5)

    quiz_item.click()
    print("✅ 퀴즈 항목 클릭 성공")
    time.sleep(0.5)    
    
    
        # ===== 퀴즈 종료 버튼 클릭 =====
    print("🛑 학습 종료 버튼 클릭 시도")

    end_learning_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH, "//a[normalize-space(text())='학습 종료']"
        ))
    )

    driver.execute_script(
        "arguments[0].scrollIntoView({block:'center'});",
        end_learning_btn
    )
    time.sleep(0.5)

    end_learning_btn.click()
    print("✅ 퀴즈 종료 버튼 클릭 성공")

    # ===== 결과 검증 =====
    WebDriverWait(driver, 10).until(
        EC.url_contains("/classrooms")
    )
    print("🏁 퀴즈 종료 후 페이지 이동 확인")
    time.sleep(3)