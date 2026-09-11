import os

def count_code_lines(root_dir):
    total_lines = 0
    for dirpath, _, filenames in os.walk(root_dir):
        for fname in filenames:
            if fname.endswith(".py"):
                full_path = os.path.join(dirpath, fname)
                with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                    for line in f:
                        stripped = line.strip()
                        if stripped:
                            total_lines +=1
    return total_lines

if __name__ == "__main__":
    target_dir = "."
    total = count_code_lines(target_dir)
    out_text = f"项目非空代码总行数：{total}"
    print(out_text)
    with open("loc_count.txt","w",encoding="utf-8") as f:
        f.write(out_text)

