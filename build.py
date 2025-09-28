#!/usr/bin/env python
import subprocess
import time
import sys

# Determine mode from command line
mode = "build"  # default
if len(sys.argv) > 1:
    if sys.argv[1] in ("--build", "--run"):
        mode = sys.argv[1][2:]  # removes the '--'

commands = []

mode = "build"

match mode:
    case "build":
        commands.append(["go", "build", "-o", "bin/app", "./cmd/server"])
    case "run":
        commands.append(["go", "run", "./cmd/server"])
    case _:
        print("Usage: ./build.py [--build | --run]")
        sys.exit(1)


for cmd in commands:
    print(f"Running: {' '.join(cmd)}")
    start_time = time.time()

    if mode == "run":
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

        try:
            for line in process.stdout:
                print(line, end="")
            process.wait()
            elapsed = time.time() - start_time
            if process.returncode == 0:
                print(f"\n✅ Finished {mode} in {elapsed:.2f}s\n")
            else:
                print(f"\n❌ Command failed after {elapsed:.2f}s")
        except KeyboardInterrupt:
            process.terminate()
            elapsed = time.time() - start_time
            print("\n⏹ Server manually terminated by user.")
            print(f"⏱ Ran for {elapsed:.2f}s")
    else:
        process = subprocess.run(cmd, check=False)
        elapsed = time.time() - start_time
        if process.returncode == 0:
            print(f"✅ Finished {mode} in {elapsed:.2f}s\n")
        else:
            print(f"❌ Command failed after {elapsed:.2f}s")
        break
