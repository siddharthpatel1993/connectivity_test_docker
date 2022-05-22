import subprocess
import re
import time

def countdown():
        t = 5
        while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print("*****Waiting Time Countdown for 5 seconds ==> ",timer, "*****")
                #print(timer,end="\r")
                time.sleep(1)
                t -= 1

        print('Times up !!!')


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
        print("Moving file/dir ", a1)
        countdown()

        subprocess.call("mv /var/log/"+ a1 +" conf/", shell=True)

if __name__=="__main__":
    url_service_function()
    #countdown()
