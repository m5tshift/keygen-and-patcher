import hashlib


def generate_key(hwid: str) -> str:
    m = hashlib.md5()
    m.update(hwid.encode("ascii"))
    digest = m.digest()  # 16 байт MD5-хеша
    rev = digest[::-1]  # разворот байтов
    return "".join(f"{b:02x}" for b in rev)


if __name__ == "__main__":
    hwid = input("Enter HWID: ").strip()
    key = generate_key(hwid)
    print("License key:", key)
