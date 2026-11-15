import subprocess

result = subprocess.run(["python", "--version"], capture_output=True, text=True)
print(result.stdout)
print(result.returncode)

out = subprocess.check_output(
    ["python", "--version"],
    text=True
)

print(out)

code = subprocess.call(["python", "--version"])
print(code)

p = subprocess.Popen(
    ["python", "--version"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

out, err = p.communicate()
print(out)

subprocess.run("dir", shell=True)

