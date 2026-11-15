import sys, traceback

try:
    x = 10 / 0
except Exception:
    traceback.print_exc()

try:
    int("abc")
except:
    err= traceback.format_exc()
    print(err)

try:
    1 / 0
except Exception:
    tb = sys.exc_info()[2]
    traceback.print_tb(tb)

try:
    1 / 0
except:
    formatted = traceback.format_exc()
    print(formatted)

try:
    1 / 0
except:
    extracted = traceback.extract_tb(tb)
    for frame in extracted:
        print(frame)