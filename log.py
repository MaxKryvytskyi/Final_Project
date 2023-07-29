from datetime import datetime as dt

def log(args, message=""):
    with open("log.txt", "a") as fn:
        date = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        fn.write(f"[{date}] {message}{args}\n")
        return args
    