import requests
import cloudscraper
import json
from datetime import datetime, timedelta
import os
from utils import get_record, save_record, Recorder


recorder = Recorder()

def init_coupon():
	raw_data = _get_coupon_data(300)
	if raw_data["result"] == "success":
		data = raw_data.get("data", None)
		record = get_record()

		if len(record["coupon"]) == 0:
			last_coupon_time = datetime.min
			new_data = []
			for d in data:
				label = d["Label"]
				create_time = d["Created"]["iso"].split(".")[0]
				create_time = datetime.strptime(create_time, "%Y-%m-%d %H:%M:%S") + timedelta(hours=8)

				if create_time <= last_coupon_time:
					break

				link = f"http://withhive.me/313/{label}"
				status = d["Status"]
				new_data.append({
					"label": label,
					"link": link,
					"create_time": str(create_time),
					"status": status
				})

			for d in new_data[::-1]:
				recorder.add_coupon(**d)


def update_coupon():
	raw_data = _get_coupon_data()
	if raw_data["result"] == "success":
		data = raw_data.get("data", None)
		record = get_record()

		last_coupon_time = datetime.strptime(record["coupon"][0]["create_time"], "%Y-%m-%d %H:%M:%S")

		new_data = []
		for d in data:
			label = d["Label"]
			create_time = d["Created"]["iso"].split(".")[0]
			create_time = datetime.strptime(create_time, "%Y-%m-%d %H:%M:%S") + timedelta(hours=8)

			if create_time <= last_coupon_time:
				break

			link = f"http://withhive.me/313/{label}"
			status = d["Status"]
			new_data.append({
				"label": label,
				"link": link,
				"create_time": str(create_time),
				"status": status
			})

		for d in new_data[::-1]:
			recorder.add_coupon(**d)

		return new_data
	else:
		return None


def _get_coupon_data(n=10):
	coupon_url = f"https://swq.jp/_special/rest/Sw/Coupon?_csrf_token=08_26MJAE2RkeZl-TSlGv6bjuutAX4FtieDYrycJ3e6d5khREGZuIuYuuhDPZOdNam_KIRdzyUfeT3_1G3o0dioOFfRNBYYXDnb2Y5CVm-1TMyo16GL9kyuXVNnTPPFRgjVtxjjbEEk&_ctx[b]=master&_ctx[c]=JPY&_ctx[l]=en-US&_ctx[t]=Asia%2FTaipei%3B%2B0800&results_per_page={n}"

	resp = cloudscraper.create_scraper(disableCloudflareV1=True, delay=10).get(coupon_url)  # 送出 requests 獲得網頁資料，headers模仿瀏覽器
	raw_data = json.loads(resp.text)
	return raw_data



if __name__ == '__main__':
	update_coupon()
	# init_coupon()
