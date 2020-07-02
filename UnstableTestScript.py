import os
import os.path
import timeit
import smtplib
'''
------- THIS SCRIPT HELPS YOU TO REPRODUCE UNSTABLE BEHAVIOUR OF REGRESSION TEST -------
---- 1. It runs design in infinit loop and checks for failures.txt file;
---- 2. Also it verifies that duration of this test is not higher then 1000s;
---- 3. After that you will have an email with attached Failures.txt, screenshot and corresponding files;
'''
os.environ["VBAE_NO_DIALOGS"] = "1"
i = 1
design = (r'C:\Users\alexey\Desktop\issue18\PCB\Route_Sketch.pcb') # designs' path directly to pcb file
failures = (r'C:\Users\alexey\Desktop\issue18\PCB\Work\Failures.txt') #
srstat = ()
screenshot = ()


# Custom function to verify timeout value;
def checktimeout(end, start):
    final = (end - start)  # duration of the test;
    timeout = float(100)  # limit in seconds for test;
    if final > timeout:
        print("Timeout On Run: {0}".format(i))
        print("Duration Of Testrun (in seconds):", final)
    else:
        print("Duration Of Testrun (in seconds):", final)
        print("No Timeout!")


# Custom function show failures.txt file in command line;
def openfile():
    f = open(r'C:\Users\alexey\Desktop\issue18\PCB\Work\Failures.txt', "r")
    print(f.read())
    f.close()


# Custom function which sends email if there is a failure;
def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('email', 'pass')
    # subject = 'Fail of the test on local machine'
    message = ('test')
    server.sendmail('from', 'who', message)
    server.quit()


# infinite loop for testing unstable tests;
while 1 == 1:
    start = timeit.default_timer()
    print("Run Number: {0}.".format(i))
    os.system(design)
    if os.path.exists(failures):
        print("Fail On Run: {0}".format(i))
        end = timeit.default_timer()
        # print("Duration Of Testrun (in seconds):", end - start)
        # openfile()
        checktimeout(end, start)
        break
    else:
        print("Successfully Finished Run: {0}".format(i))
        end = timeit.default_timer()
        checktimeout(end, start)
        i += 1
        # print("Duration Of Testrun (in seconds):", end - start)