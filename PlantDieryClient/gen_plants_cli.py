import json, requests
from termcolor import colored

GREEN_LINE = colored("-----------------------------", 'green')
YELLOW_LINE = colored("-----------------------------", 'yellow')

API_URL = "http://127.0.0.1:5000/api"

class GeneralPlant():
	def add_general_plant(self):
		print(YELLOW_LINE)
		print(colored("  Add new general plant", 'yellow'))
		print(YELLOW_LINE)
		plant_data = {}
		# Todo: Add checks
		inp = input("Give plant's specie: ")
		if not inp:
			return print(colored("Specie cannot be null, try again", 'red'))
		plant_data["specie"] = inp

		inp = input("Give care instructions: ")
		if not inp:
			return print(colored("\nInstruction cannot be null, try again\n", 'red'))	
		plant_data["instruction"] = inp

		inp = input("Give watering instuctions (optional): ")
		plant_data["water"] = inp

		inp = input("Give suitable soil (optional): ")
		plant_data["soil"] = inp

		r = requests.post(API_URL + "/plantsgeneral/", data=json.dumps(plant_data),
			headers={"Content-type": "application/json"})

		if r.status_code != 201:
			print("\nstatus : " + str(r.status_code))
			print(colored("Something went wrong, try again \n", 'red'))
		else:
			print(colored("\n!!New general plant added!!\n", 'green'))
		return 

	def modify_general_plant(self):
		print(YELLOW_LINE)
		print("  Modify saved general plant")
		print(YELLOW_LINE)   
		plant_data = {}

		gpid = input("Give if of general plant to be modified: ")
		if not gpid:
			return print("id can't be null\n")
		plant_data["id"] = gpid

		specie = input("Give new specie: ")
		if not specie:
			return print("Specie can't be null\n")
		plant_data["specie"] = specie

		ins = input("Give new caring instructions: ")
		if not ins:
			return print("Instructions can't be null")
		plant_data["instruction"] = ins

		water = input("Give new watering info: ")
		plant_data["water"] = water

		soil = input("Give new soil: ")
		plant_data["soil"] = soil

		r = requests.put(API_URL + "/plantsgeneral/{}/".format(id), data=json.dumps(plant_data),
			headers={"Content-type": "application/json"})
		if r.status_code != 204:
			print("\nstatus : " + str(r.status_code))
			print("msg : " + str(r.text))
			print(colored("Something went wrong, try again\n", "red"))
			return
		return print(colored("\n!!General plant updated!!\n", 'green'))


	def delete_general_plant(self):
		print(YELLOW_LINE)
		print("  Delete saved generalplant")
		print(YELLOW_LINE)
		plantid = input("Give id of the general plant to be deleted: ")
		if not plantid:
			return print(colored("Id can't be null", 'red'))
		r = requests.delete(API_URL + "/plantsgeneral/{}/".format(plantid))
		if r.status_code != 204:
			print("Status : " + str(r.status_code))
			print(colored("Something went wrong, try again\n", 'red'))
			return
		print(colored("\n!!Plant {} delete success!!\n", 'green'))
			

	def get_all_general_plants(self):
		print(YELLOW_LINE)
		print("  All saved general plants")
		print(YELLOW_LINE)
		resp = requests.get(API_URL + "/plantsgeneral/")
		try:
			body = resp.json()
		except ValueError:
			return print(colored("\nNO GENERAL PLANTS SAVED\n", 'red'))
		for item in body["items"]:
			print(GREEN_LINE)
			print("Id: " + str(item["id"]))
			print("Specie : " + str(item["specie"]))
			print(GREEN_LINE + "\n")
		return 
		
	def get_single_general_plant(self):
		print(YELLOW_LINE)
		print("  General plant's information")
		print(YELLOW_LINE)
		giv_input = input("Give general plant's id: ")
		print(GREEN_LINE)

		if not giv_input:
			return print(colored("\nId can't be null\n", 'red'))
		print("\n")
		try:
			resp = requests.get(API_URL + "/plantsgeneral/{}/".format(giv_input))
			body = resp.json()
			print(GREEN_LINE)
			print("Specie : " + body["specie"])
		except (ValueError, KeyError):
			print("No plant with id {} saved".format(giv_input))
		
		print(GREEN_LINE)
		print("Instructions: " + str(body["instruction"]))
		print("Watering: " + str(body["water"]))
		print("Soil: " + str(body["soil"]))
		print(GREEN_LINE + "\n")
		return

	def __init__(self):
		pass