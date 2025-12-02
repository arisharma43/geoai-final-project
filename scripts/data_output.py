from pathlib import Path

dir_candidates = [Path("D:/Coding/geoai-final-project/data/small/48201C_20251130")]

for d in dir_candidates:
    if d.exists() and d.is_dir():
        files = sorted([p.name for p in d.iterdir() if p.is_file()])
        if files:
            print(f"Files in {d}:")
            for name in files:
                print(name)
        else:
            print(f"No files found in {d}")
        break
else:
    print("Directory not found. Checked:")
    for d in dir_candidates:
        print(f" - {d}")
