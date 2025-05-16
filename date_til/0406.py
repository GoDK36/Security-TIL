import re

def check_password_strength(password):
    """간단한 암호 강도 검사 함수"""
    score = 0

    # 길이 검사
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # 복잡성 검사
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#%^&*\(\),.?\":{|<>}]", password):
        score += 1

    # 결과 해석
    if score <= 2:
        return "weak"
    elif score <= 4:
        return "soso"
    else:
        return "strong"
    

# 테스트
test_passwords = ["password", "Password1", "P@ssw0rd!", "Str0ng_P@ssw0rd_2023!"]
for pwd in test_passwords:
    print(f"암호: {pwd} - 강도: {check_password_strength(pwd)}")
    