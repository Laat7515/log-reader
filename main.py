version = '0.0.1'
print('Log-reader version', version)
##
##
result = open('log.txt', 'w')
result.write("")
result.close()

file = open('access.log', 'r')
ip = str(file.readline(15))
result = open('log.txt', 'a')
count = 0
ipcount = 0
with open('access.log', 'r') as f:
    for line in f:
        count += 1
        ipTest = str(f.readline(15))
        result.writelines(ipTest)
        result.writelines("\n")
        if ip == ipTest:
            ipcount += 1
            pass
print(ipTest)
print("IP " + str(ip) +" was found " + str(ipcount) + " times")
print("Total number of lines is:", count)

f.close()
file.close()