import urllib.request

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour='0-16', second='*/10')
def scheduled_job():
	url = "https://summoners-coupon.herokuapp.com/"
	conn = urllib.request.urlopen(url)

	print("=============== Awake Heroku start ===============")
	for key, value in conn.getheaders():
		print(key, value)
	print("=============== Awake Heroku end ===============")

# scheduled_job()
sched.start()




