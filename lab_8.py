#1
ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "192.168.1.10"]
unique_ips = set(ips)
print(unique_ips)
#2
blocked = {"root", "admin", "test"}
blocked.add("hacker")
blocked.remove("test")
print(blocked)
#3
forbidden = {21, 22, 23, 25}
port = 22

if port in forbidden:
    print("Порт запрещён")
else:
    print("Порт разрешён")
#4
known = {"mal.com", "bad.net"}
new = {"bad.net", "xevil.org"}

not_in_base = new.difference(known)
print(not_in_base)
#5
white = {"alice", "bob", "root"}
black = {"root", "admin"}

conflict = white.intersection(black)
print(conflict)
#6
a = {"CVE-1", "CVE-2"}
b = {"CVE-2", "CVE-3"}

all_vulns = a.union(b)
print(all_vulns)
#7
admin = {"read", "write", "delete"}
user = {"read", "download"}

diff = admin.symmetric_difference(user)
print(diff)
#8
logs = ["123", "qwerty", "test", "123", "qwerty", "admin"]
blocked = {"test"}

unique = set(logs)
filtered = unique.difference(blocked)
print(filtered)
#9
global_ips = { "10.0.0.1", "10.0.0.2", "192.168.1.1" }
local_ips = { "10.0.0.2", "10.0.0.3" }

local_ips.intersection_update(global_ips)
print(local_ips)
#10
logs = ["scan", "debug_mode", "scan", "connect", "debug_info"]

unique = set(logs)
filtered = {cmd for cmd in unique if "debug" not in cmd}

print(filtered)

