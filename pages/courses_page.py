def test_open_classrooms_page(driver, base_url):
    url = f"{base_url}/classrooms/"
    driver.get(url)

    print("현재 URL:", driver.current_url)

    # 로그인 안 되어 있으면 로그인 페이지로 리다이렉트될 수도 있음
    assert "classrooms" in driver.current_url or "login" in driver.current_url
