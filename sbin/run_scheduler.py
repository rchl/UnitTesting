from .unittesting import run_scheduler

import sys

def write_log(txt):
    if sys.platform.startswith("win"):
        with open("c:/st/out.txt", "a+") as f:
            f.write(txt + "\n")

# sys.stdout = StdioSplitter(sys.stdout, rf)
# sys.stderr = StdioSplitter(sys.stderr, rf)


def plugin_loaded():
    try:
        write_log("run_scheduler")
        run_scheduler()

    except Exception as e:
        write_log(str(e))
