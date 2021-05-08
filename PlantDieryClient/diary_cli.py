import json, requests
from termcolor import colored
from datetime import datetime
from plants_cli import Plant

API_URL = "http://127.0.0.1:5000/api"
GREEN_LINE = colored("---------------------------------------", 'green')
YELLOW_LINE = colored("---------------------------------------", 'yellow')

class Diary:
	def get_all_entries(self):
		print(YELLOW_LINE)
		print(colored("  Plant diary", 'white'))
		print(YELLOW_LINE)
		resp = requests.get(API_URL + "/plantdiary/")
		try:
			body = resp.json()
		except ValueError:
			return print(colored("Empty diary", 'red'))
		print(GREEN_LINE)
		for item in body["items"]:
			print(colored("Id: " + str(item["id"]), 'blue'))
			print("Date: " + str(item["date"]))
			print(colored("Plant: " + str(item["plant"]), 'magenta'))
			print("Description: " + str(item["description"]))
			print("Watering: " + str(item["water_info"]))
			print("Wellbeing: " + str(item["wellbeing"]))
			print(GREEN_LINE)
		return print("\n")

	def add_entry(self):
		print(YELLOW_LINE)
		print(colored("  Add new diary entry", 'yellow'))
		print(YELLOW_LINE)
		diary_data = {}
		inp = input("Give plant's name for diary entry: ")
		if not inp:
			return print(colored("Name can't be null, try again", 'red'))
		diary_data["plant"] = inp
		inp = input("Description: ")
		if not inp:
			return print(colored("Description can't be empty, try again", 'red'))
		diary_data["description"] = inp
		inp = input("Watering today (optional): ")
		diary_data["water_info"] = inp

		inp = input("Overall wellbeing (optional): ")
		diary_data["wellbeing"] = inp	

		diary_data["date"] = str(datetime.now())

		r = requests.post(API_URL + "/plantdiary/", data=json.dumps(diary_data),
			headers={"Content-type": "application/json"})

		if r.status_code != 201:
			print("\nstatus : " + str(r.status_code))
			print("text: " + str(r.text))
			return print(colored("Something went wrong, try again\n", 'red'))		
		return print(colored("\n!!New entry added!!\n", 'green'))

	def delete_entry(self):
		print(YELLOW_LINE)
		print(colored("  Delete diary entry", 'yellow'))
		print(YELLOW_LINE)
		inp = input("Give diary entry id : ")
		if not inp:
			return print(colored("Id can't be null, try again", 'red'))  
		r = requests.delete(API_URL + "/plantdiary/{}/".format(inp))
		if r.status_code != 204:
			print("\nStatus : " + str(r.status_code))
			print(colored("Something went wrong, try again\n", 'red'))
		print(colored("\n!!Entry {} delete success!!\n".format(inp), 'green'))