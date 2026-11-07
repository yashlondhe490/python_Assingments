import os
import re

for f in os.listdir("."):
    m = re.match(r"^(\d+)_.+\.py$", f)   # matches 1_whileloopExample.py etc.
    if m:
        new = f"{m.group(1)}_.py"          # becomes 1_.py
        if os.path.exists(new):
            print("SKIPPED (already exists):", f)
        else:
            os.rename(f, new)
            print(f, "->", new)