import urllib.request

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour='0-16', minute='*/20')
def scheduled_job():
	url = "https://summoners-coupon.herokuapp.com/"
	conn = urllib.request.urlopen(url)

	print("=============== Awake Heroku start ===============")
	print(f"url: {url}")
	for key, value in conn.getheaders():
		print(key, value)
	print("=============== Awake Heroku end ===============")

@sched.scheduled_job('cron', hour='16')
def awake_heroku_caller():
	url = "https://awake-each-heroku.herokuapp.com/"

	conn = urllib.request.urlopen(url)
	print("=============== Awake Heroku start ===============")
	print(f"url: {url}")
	for key, value in conn.getheaders():
		print(key, value)
	print("=============== Awake Heroku end ===============")

sched.start()




