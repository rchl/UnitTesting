from .unittesting import run_scheduler

import sys

def write_log(txt):
    if sys.platform.startswith("win"):
        with open("c:/st/out.txt", "a+") as f:
            f.write(txt + "\n")

# sys.stdout = StdioSplitter(sys.stdout, rf)
# sys.stderr = StdioSplitter(sys.stderr, rf)


try:
    write_log("run_scheduler")
    run_scheduler()

except Exception as e:
    with open("c:/st/out.txt", "a+") as f:
        write_log(str(e))
