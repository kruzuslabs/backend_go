#!/usr/bin/env python
import subprocess
import time
import sys

# Determine mode
mode = sys.argv[1][2:] if len(sys.argv) > 1 else "build"

match mode:
    case "build":
        cmd = ["go", "build", "-o", "bin/app", "./cmd/server"]
    case "run":
        cmd = ["go", "run", "./cmd/server"]
    case "release":
        cmd = ["go", "build", "-ldflags", "-s -w", "-o", "bin/app", "./cmd/server"]
    case _:
        print("Usage: ./build.py [--build | --run | --release]")
        sys.exit(1)


print(f"Running: {' '.join(cmd)}")
start_time = time.time()

if mode == "run":
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    try:
        for line in process.stdout:
            print(line, end="")
        process.wait()
        ret = process.returncode
    except KeyboardInterrupt:
        process.terminate()
        ret = -1
        print("\n⏹ Server manually terminated by user.")
else:
    process = subprocess.run(cmd)
    ret = process.returncode

elapsed = time.time() - start_time
if ret == 0:
    print(f"\n✅ Finished {mode} in {elapsed:.2f}s")
 
