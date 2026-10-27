import os
import re

folder = r"C:\Python_programs\LoopingStatements"   # change this path

for f in os.listdir(folder):
    m = re.match(r"^(\d+)_.+\.py$", f)
    if m:
        new = f"{m.group(1)}_.py"
        old_path = os.path.join(folder, f)
        new_path = os.path.join(folder, new)
        if os.path.exists(new_path):
            print("SKIPPED (already exists):", f)
        else:
            os.rename(old_path, new_path)
            print(f, "->", new)