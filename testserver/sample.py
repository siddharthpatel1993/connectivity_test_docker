import subprocess
import re
import time

def url_service_function():
    x = subprocess.check_output("cat configuration_and_log/test.txt | grep -v '^#' | sed '/^$/d;s/[[:blank:]]//g' > configuration_and_log/test1.txt", shell=True)

    # Using readlines()
    file1 = open('configuration_and_log/test1.txt', 'r')
    Lines = file1.readlines()
    file1.close()

    count = 0
    #Strips the newline character
    for line in Lines:
        count = count + 1
        host_num = count

        a1 = "{}".format(line.strip())
        print(a1)

        subprocess.call("mv /var/log/"+ a1 +" conf/", shell=True)

if __name__=="__main__":
    url_service_function()
