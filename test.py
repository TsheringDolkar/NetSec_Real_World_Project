import subprocess


def gateNet(desire):
    if desire == 0:
        cmd = "ip route | grep default | awk '{print $3}'"
    elif desire == 1:
        cmd = "ip route | grep / | awk '{print $1}'"
    ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    output = (ps.communicate()[0]).decode("UTF-8")
    return (output.split("\n"))[0]


a=gateNet(1)
print(a)
print(type(a))