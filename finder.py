import subprocess


results = str(subprocess.check_output(["netsh", "wlan", "show", "network"])
              .decode('utf-8', errors="backslashreplace")
              .replace("\r",""))

ls = results.split("\n")
ls = ls[4:]
ssids = []
x = 0
while x < len(ls):
    if x % 5 == 0:
        ssids.append(ls[x])
    x += 1
print(ssids)