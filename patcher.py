import os


def patch_program(filename):
    # MOV dword ptr [RBP + local_24], 0
    # C7 45 E4 00 00 00 00
    search_pattern = b"\xc7\x45\xe4\x00\x00\x00\x00"

    # MOV dword ptr [RBP + local_24], 1
    # C7 45 E4 01 00 00 00
    replace_pattern = b"\xc7\x45\xe4\x01\x00\x00\x00"

    if not os.path.exists(filename):
        print(f"Файл '{filename}' не найден.")
        return

    with open(filename, "rb") as f:
        data = f.read()

    if search_pattern in data:
        print("Сигнатура найдена.")
        new_data = data.replace(search_pattern, replace_pattern)

        patched_filename = filename + "_patched"
        with open(patched_filename, "wb") as f:
            f.write(new_data)

        os.chmod(patched_filename, 0o755)
        print(f"Патч успешно применен. Создан файл: {patched_filename}")
    else:
        print("Ошибка.")


if __name__ == "__main__":
    target_file = "hack_app"
    patch_program(target_file)
