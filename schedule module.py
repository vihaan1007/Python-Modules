import schedule, time

def job():
    print("Task running")
def fob():
    print("Task")

schedule.every(5).seconds.do(job)#replace second with minute or hour if needed 
#for daily- schedule.every().day.at("10:30").do(job)
#for weekly- schedule.every().monday.at("10:30").do(job)

#cumpolsury
a = 0
while a <= 10:
    schedule.run_pending()
    time.sleep(1)# to not kill the CPU on high levels
    a += 1

jobb= schedule.every(2).seconds.do(fob)
schedule.cancel_job(jobb)#jobb clear
#schedule.clear() all clear
