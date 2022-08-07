import os
import json

record_template = {
	"user": [],
	"coupon": [],
}

def get_record():
	if not os.path.isfile("record.json"):
		record = record_template
		save_record(record)
	else:
		with open("record.json", 'r') as file:
			content = file.read()
			record = json.loads(content) if content.strip() != "" else record_template
	return record


def save_record(record):
	with open("record.json", 'w') as file:
		print(json.dumps(record, indent=4), file=file)


class Recorder:
	def __init__(self):
		pass

	# User Function
	def add_user(self, user_id):
		record = get_record()
		if user_id not in record["user"]:
			print(f"add user: {user_id}")
			record["user"].append(user_id)
			save_record(record)
			return True
		return False

	def remove_user(self, user_id):
		record = get_record()
		if user_id in record["user"]:
			print(f"remove user: {user_id}")
			record["user"].remove(user_id)
			save_record(record)
			return True
		return False

	def get_all_user(self):
		record = get_record()
		return record["user"]

	# Coupons Function
	def add_coupon(self, label, link, create_time, status):
		record = get_record()
		if label not in record["coupon"]:
			new_coupon = {
				"label": label,
				"link": link,
				"create_time": create_time,
				"status": status,
			}
			record["coupon"] = [new_coupon] + record["coupon"]
			save_record(record)
			print(f"Add coupon: {label}")
