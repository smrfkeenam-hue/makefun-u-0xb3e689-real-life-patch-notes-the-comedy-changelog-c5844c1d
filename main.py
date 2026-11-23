import os

ENTRY = "v2.4.1: fixed a bug where a sneeze also triggered the bladder's emergency release valve. Systems now queue politely."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
