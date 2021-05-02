import subprocess
import re
import time

def url_service_function():
    x = subprocess.check_output("cat configuration_and_log/configuration_url_service.txt | grep -v '#' | sed '/^$/d;s/[[:blank:]]//g' > configuration_and_log/configuration.txt", shell=True)

    # Using readlines()
    file1 = open('configuration_and_log/configuration.txt', 'r')
    Lines = file1.readlines()
    file1.close()

    count = 0
    #Strips the newline character
    for line in Lines:
        count = count + 1
        host_num = count

        a1 = "{}".format(line.strip())
        #print(a1)

        s0 = re.compile(r'^[A-Za-z-0-9_ ]+[=]')
        m0 = s0.search(a1)
        if m0:
            service_name = m0.group()
            print("Service Name ==> "+ service_name.rstrip('=') +"")
        s1 = re.compile(r'[/][/](.*)[/]')
        m1 = s1.search(a1)
        #print(m1.group(1))
        if m1:
            #print(m1.group(1))
            a2 = m1.group(1)
            s2 = re.compile(r'(.*)[:](.*)')
            m2 = s2.search(a2)
            #print(m2.group(0))
            if m2:
                #print(m2.group(0))
                a3 = m2.group(0)
                #print(m2.group(0))
                s3 = re.compile(r'(.*)[:]')
                m3 = s3.search(a3)
                host = m3.group(1)
                print("Host "+ str(host_num) +" ==> "+ host +"")
                s4 = re.compile(r'[:][0-9]+')
                m4 = s4.search(a3)
                port = m4.group().strip(':')
                print("Port ==> "+ port +"")
                y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)

            else:
                s5 = re.compile(r'[/][/](.*)[/]')
                m5 = s5.search(a1)
                s6 = re.compile(r'[/][/][a-z0-9]+[.][a-z]+[.][a-z]+')
                m6 = s6.search(a1)
                if m6:
                    #print(m5.group())
                    host = m6.group().lstrip('//')
                    print("Host "+ str(host_num) +" ==> "+ host +"")
                    s7 = re.compile(r'[=](.*)[:]')
                    m7 = s7.search(a1)
                    #print(m5.group(1))
                    a5 = m7.group(1).lstrip()
                    if (a5 == 'http'):
                        print("As it is http, and port is not mentioned so using default port 80")
                        port = '80'
                        print("Port ==> "+ port +"")
                        y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                        print("********************Done****************")
                        time.sleep(3)
                        continue
                    elif(a5 == 'https'):
                        print("As it is https, and port is not mentioned so using default port 443")
                        port = '443'
                        print("Port ==> "+ port +"")
                        y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                        print("********************Done****************")
                        time.sleep(3)
                        continue
                    else:
                        print("It is neither http not https")
                        print("********************Done****************")
                        time.sleep(3)
                        continue
                if m5:
                    host1 = m5.group(1)
                    s8 = re.compile(r'^[A-Za-z0-9.-]+')
                    m8 = s8.search(host1)
                    host = m8.group()
                    print("Host "+ str(host_num) +" ==> "+ host +"")
                    s9 = re.compile(r'[=](.*)[:]')
                    m9 = s9.search(a1)
                    #print(m9.group(1))
                    a5 = m9.group(1).lstrip()
                    if (a5 == 'http'):
                        print("As it is http, and port is not mentioned so using default port 80")
                        port = '80'
                        print("Port ==> "+ port +"")
                        y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                        print("********************Done****************")
                        time.sleep(3)
                        continue
                    elif(a5 == 'https'):
                        print("As it is https, and port is not mentioned so using default port 443")
                        port = '443'
                        print("Port ==> "+ port +"")
                        y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                        print("********************Done****************")
                        time.sleep(3)
                        continue

                    print("********************Done****************")
                    time.sleep(3)
                    continue

            print("********************Done****************")
            time.sleep(3)
        
        else:
            #print(a1)
            s10 = re.compile(r'[/][/](.*)[:](.*)')
            m10 = s10.search(a1)
            if m10:
                fqdn = m10.group()
                #print(fqdn)
                s11 = re.compile(r'[/][/](.*)[:](.*)')
                m11 = s11.search(fqdn)
                host = m11.group(1)
                print("Host "+ str(host_num) +" ==> "+ host +"")
                s12 = re.compile(r'[:](.*)')
                m12 = s12.search(fqdn)
                port = m12.group(1)
                print("Port ==> "+ port +"")
                y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                print("********************Done****************")
                time.sleep(3)
                continue
 
            s13 = re.compile(r'[/][/](.*)')
            m13 = s13.search(a1)
            if m13:
                host = m13.group(1)
                print("Host "+ str(host_num) +" ==> "+ host +"")
                s14 = re.compile(r'[=](.*)[:]')
                m14 = s14.search(a1)
                #print(m14.group(1))
                a5 = m14.group(1).lstrip()
                if (a5 == 'http'):
                    print("As it is http, and port is not mentioned so using default port 80")
                    port = '80'
                    print("Port ==> "+ port +"")
                    y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                    print("********************Done****************")
                    time.sleep(3)
                    continue
                elif(a5 == 'https'):
                    print("As it is https, and port is not mentioned so using default port 443")
                    port = '443'
                    print("Port ==> "+ port +"")
                    y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                    print("********************Done****************")
                    time.sleep(3)
                    continue
            
            s15 = re.compile(r'=(.*)')
            m15 = s15.search(a1)
            if m15:
                host = m15.group(1)
                print("Host "+ str(host_num) +" ==> "+ host +"")
                port = '25'
                print("Port ==> "+ port +"")
                y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)
                print("********************Done****************")
                time.sleep(3)
                continue

    print("********************Completed****************")

def manual_change_function():
    x = subprocess.check_output("cat configuration_and_log/configuration_manual_change.txt | grep -v '#' | sed '/^$/d;s/[[:blank:]]//g' > configuration_and_log/configuration1.txt", shell=True)

    # Using readlines()
    file2 = open('configuration_and_log/configuration1.txt', 'r')
    Lines = file2.readlines()
    file2.close()

    count = 0
    #Strips the newline character
    for line in Lines:
        count = count + 1
        host_num = count

        a2 = "{}".format(line.strip())
        #print(a2)

        s0 = re.compile(r'^[a-zA-Z0-9_]+,')
        m0 = s0.search(a2)
        service_name = m0.group().rstrip(',')
        print("Service Name ==> "+ service_name +"")

        s1 = re.compile(r'[,][a-zA-Z0-9_.-]+[:]')
        m1 = s1.search(a2)

        host= (m1.group(0).rstrip(':')).lstrip(',')
        print("Host "+ str(host_num) +" ==> "+ host +"")

        s2 = re.compile(r'[:][0-9]+')
        m2 = s2.search(a2)
        port = m2.group().lstrip(':')
        print("Port ==> "+ port +"")
        
        y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)

        print("********************Done****************")
        time.sleep(3)

    print("********************Completed****************")

def manual_input():
    n = int(input("Enter the number of servers you have for test\n"))
    print("*****************Checking the connection starts****************")

    for i in range (n):
        count = i + 1
        host = str(input("Enter the "+ str(count) +" host\n"))
        port = str(input("Enter the port\n"))

        y = subprocess.call("nc -vz -w 5 "+ host +" "+ port +"", shell=True)

        print("********************Done****************")

    print("********************Completed****************")
        
if __name__=="__main__":
    print('''Press 1 for URL service type connectivity test
Press 2 for Manual configuration type connectivity test
Press 3 for giving input of host and port from keyboard everytime''')
    option = int(input())
    if( option == 1 ):
        print("*****************Checking the connection starts****************")
        url_service_function()
    elif( option == 2 ):
        print("*****************Checking the connection starts****************")
        manual_change_function()
    elif( option == 3 ):
        manual_input()
    else:
        print("You gave wrong choice, pls give right input")
