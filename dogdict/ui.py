import json
import requests


# check_for_space needs to be imported from utils
#from dogdict import check_for_space

API_URL = "http://localhost:5000"

def check_for_space(name):
    #print("checking whether name had a space")
    if " " in name:
        split_by_space = name.split()
        for word in split_by_space:
            if not word.isalpha():
                raise BadRequest(
                f"'{name}' contains unsupported characters. \
                    Only letters and 'space' allowed."
            )
        #print("name had a space... converting...")
        name = name.replace(" ", "%20")
    
    return name

def prompt_from_schema(session, ctrl, **kwargs):
    """
    Acquire schema and get user inputs
    """

    try:
        schema = ctrl["schema"]
    except KeyError:
        schema = session.get(ctrl["schemaUrl"]).json()

    model = kwargs.get("model", None)
    breed = kwargs.get("breed", None)
    group = kwargs.get("group", None)
    edited_fact = kwargs.get("data", None)


    if model == "characteristics":
        schema["required"].append("exercise")
        schema["required"].append("coat_length")
        
        schema["properties"].update(
            {'exercise': {'description': 'Amount of daily exercise (0-5)',
                                                   'type': 'number'}})
        schema["properties"].update(
            {'coat_length': {'description': 'Coat length of a breed (0-1)',
                                                      'type': 'number'}})

    data = {}
    for item in schema["required"]:
        item_prompt = None


        if item == "breed" or item == "group":
            if (breed is None) or (group is None):
                item_prompt_str = str(schema["properties"][item]["description"] + ": ")
                item_prompt = input(item_prompt_str)
            else:
                if item == "breed":
                    item_prompt = breed
                if item == "group":
                    item_prompt = group
        if item == "coat_length" or item == "exercise":
            print(f"Choose y to input {item} characteristic, enter to skip")
            more_chars = input("Selection: ")
            if more_chars == "":
                continue
        if item == "fact":
            if edited_fact is None:
                item_prompt_str = str(schema["properties"][item]["description"] + ": ")
                item_prompt = input(item_prompt_str)
            else:
                item_prompt = edited_fact

        if item_prompt is None:
            item_prompt_str = str(schema["properties"][item]["description"] + ": ")
            item_prompt = input(item_prompt_str)
        

        item_type = schema["properties"][item]["type"]

        if item_type == "string":
            item_prompt = str(item_prompt)

        if item_type == "integer":
            item_prompt = int(item_prompt)

        if item_type == "number":
            item_prompt = float(item_prompt)

        data[item] = item_prompt

    return submit_data(session, ctrl, data)

def delete_from_prompt(session_object, ctrl, **kwargs):
    """
    delete data
    """
    print(kwargs)
    model = kwargs.get("model", None)
    group = kwargs.get("group", None)
    breed = kwargs.get("breed", None)

    if model == "fact":
        resp = session_object.get(API_URL + f"/api/groups/{group}/breeds/{breed}/facts/")
        body = resp.json()
        facts = {}
        print(f"\nFacts for breed:")
        for item in body["items"]:
            facts[item["fact_id"]] = item["fact"]
            print(item["fact_id"], " - ", item["fact"])

        fact_to_delete = input("Select a fact to delete: ")
        ctrl["href"] = ctrl["href"] + fact_to_delete + "/"
    response = session_object.request(
        "DELETE",
        API_URL + ctrl["href"]
    )
    return response


def submit_data(session_object, ctrl, data):
    """
    submit data
    """

    response = session_object.request(
        ctrl["method"],
        API_URL + ctrl["href"],
        data=json.dumps(data),
        headers = {"Content-type": "application/json"}
    )
    return response

def get(s):
    print("\nTo fetch all groups, choose 1")
    print("To fetch all breeds from a group, choose 2")
    print("To fetch all facts from a group and a breed, choose 3")
    print("To fetch all characteristics from a group and a breed, choose 4")
    print("\nTo go back, choose b")
    print("To exit the program, choose e\n")

    user_input = input("Selection: ")

    if user_input == "e":
        print("exiting the program...")
        exit()
    
    if user_input == "b":
        print("going back...")
        return user_input
    
    if user_input == "1":
        resp = s.get(API_URL + "/api/groups/")
        body = resp.json()
        print("Names of all groups:\n")
        for item in body["items"]:
            print(item["name"])
        print("\n")
        return

    if user_input == "2":
        group = input("Group name: ")

        group_url = check_for_space(group)

        resp = s.get(API_URL + "/api/groups/" + group_url)
        body = resp.json()

        print("\nNames of all breeds in group {}:".format(group))
        for item in body["items"]:
            for breed in item["breeds"]:
                print(breed)
        print("\n")
        return


    if user_input == "3":
        group = input("Group name: ")
        breed = input("Breed name: ")

        group_url = check_for_space(group)
        breed_url = check_for_space(breed)

        resp = s.get(API_URL + "/api/groups/" + group_url + "/breeds/" 
                     + breed_url + "/" + "facts")
        body = resp.json()

        if len(body["items"]) == 0:
            print(f"\n{breed} does not have any facts yet.\n")
            return
        print("\nAll facts from breed {} in group {}:\n".format(breed, group))
        for item in body["items"]:
            print(item["fact"])
        print("\n")
        return

    if user_input == "4":
        group = input("Group name: ")
        breed = input("Breed name: ")

        group_url = check_for_space(group)
        breed_url = check_for_space(breed)

        resp = s.get(API_URL + "/api/groups/" + group_url + "/breeds/" 
                     + breed_url + "/" + "characteristics")
        body = resp.json()

        if len(body["items"]) == 0:
            print(f"\n{breed} does not have any characteristics yet.\n")
            return

        print("\nAll characteristics from breed {} in group {}:\n".format(breed, group))
        print("coat_length: ", body["items"][0]["coat_length"], " m")
        print("life_span: ", body["items"][0]["life_span"], " years")
        print("exercise: ", body["items"][0]["exercise"], " hours/day")
        print("\n")
        return

    else:
        print("\nInvalid input, try again")
        get(s)


def post(s):
    print("\nTo add a new group, choose 1")
    print("To add a new breed, choose 2")
    print("To add a new fact, choose 3")
    print("To add a new set of characteristics, choose 4")
    print("\nTo go back, choose b")
    print("To exit the program, choose e\n")

    user_input = input("Selection: ")

    if user_input == "e":
        print("exiting the program...")
        exit()
    
    if user_input == "b":
        print("going back...")
        return user_input
    
    if user_input == "1":
        resp = s.get(API_URL + "/api/groups/")
        body = resp.json()

        response = prompt_from_schema(s, body["@controls"]["groups:add-group"])

        if response.status_code == 201:
            print("\nNew group successfully added\n")
            return
        
        else:
            if response.status_code == 409:
                print("Group already exists.")
            else:
                print(f"Error with response code {response.status_code} occurred.")
                print("Try again.")
            post(s)

    if user_input == "2":
        group = input("Group name: ")

        group_url = check_for_space(group)

        resp = s.get(API_URL + f"/api/groups/{group_url}/breeds/")
        if resp.status_code == 404:
            print(f"Group {group} was not found. Try again.\n")
            return
        body = resp.json()

        response = prompt_from_schema(s, body["@controls"]["breeds:add-breed"])


        if response.status_code == 201:
            print("\nNew breed successfully added\n")
            return
        
        else:
            if response.status_code == 409:
                print("Breed already exists.")
            else:
                print(f"Error with response code {response.status_code} occurred.")
                print("Try again.")
            post(s)
        
    if user_input == "3":
        group = input("Group name: ")
        breed = input("Breed name: ")

        group_url = check_for_space(group)
        breed_url = check_for_space(breed)

        resp = s.get(API_URL + f"/api/groups/{group_url}/breeds/{breed_url}/facts/")
        if resp.status_code == 404:
            print(f"{breed} in group {group} not found. Try again\n")
            return

        body = resp.json()

        response = prompt_from_schema(s, body["@controls"]["facts:add-fact"],
                                      breed=breed, group=group)


        if response.status_code == 201:
            print("\nNew fact successfully added")
            return
        
        else:
            if response.status_code == 409:
                print("Fact already exists.")
            else:
                print(f"Error with response code {response.status_code} occurred.")
                print("Try again.")
            post(s)

    if user_input == "4":
        group = input("Group name: ")
        breed = input("Breed name: ")

        group_url = check_for_space(group)
        breed_url = check_for_space(breed)

        resp = s.get(API_URL + f"/api/groups/{group_url}/breeds/{breed_url}/characteristics/")
        if resp.status_code == 404:
            print(f"{breed} in group {group} not found. Try again\n")
            return
        body = resp.json()

        response = prompt_from_schema(s, body["@controls"]["characteristics:add-characteristic"],
                                      breed=breed, group=group, model="characteristics")


        if response.status_code == 201:
            print("\nNew set of characteristics successfully added\n")
            return
        
        else:
            if response.status_code == 409:
                print("Chars already exists. Perhaps you meant to update existing ones?")
            else:
                print(f"Error with response code {response.status_code} occurred.")
                print("Try again.")
            post(s)


    else:
        print("\nInvalid input, try again")
        post(s)

def delete(s):
    print("\nTo delete a breed from a group, choose 1")
    print("To delete a fact from a breed, choose 2")
    print("\nTo go back, choose b")
    print("To exit the program, choose e\n")

    user_input = input("Selection: ")

    if user_input == "e":
        print("exiting the program...")
        exit()
    
    if user_input == "b":
        print("going back...")
        return user_input
    
    if user_input == "1":
        group = input("Group name: ")
        breed = input("Breed name: ")

        group_url = check_for_space(group)
        breed_url = check_for_space(breed)

        resp = s.get(API_URL + f"/api/groups/{group_url}/breeds/{breed_url}")
        if resp.status_code == 404:
            print(f"Group {group} was not found. Try again.\n")
            return
        body = resp.json()

        response = delete_from_prompt(s, body["@controls"]["breed:delete"],
                                      group=group, breed=breed)
        
        if response.status_code == 204:
            print("\nBreed successfully deleted\n")
            return

        else:
            print("Group not deleted")
            delete(s)

    if user_input == "2":
        group = input("Group name: ")
        breed = input("Breed name: ")

        group_url = check_for_space(group)
        breed_url = check_for_space(breed)

        resp = s.get(API_URL + f"/api/groups/{group_url}/breeds/{breed_url}/facts/")
        if resp.status_code == 404:
            print(f"{breed} in group {group} not found. Try again\n")
            return

        body = resp.json()


        response = delete_from_prompt(s, body["@controls"]["facts:facts-all"],
                                      breed=breed_url, group=group_url, model="fact")


        if response.status_code == 204:
            print("\nFact sucessfully deleted\n")
            return
        
        else:
            if response.status_code == 409:
                print("IntegrityError.")
            else:
                print(f"Error with response code {response.status_code} occurred.")
                print("Try again.")
            delete(s)

    else:
        print("\nInvalid input, try again")
        delete(s)

def put(s):
    print("\nTo update a group, choose 1")
    print("To update a breed in a group, choose 2")
    print("To update breed's fact, choose 3")
    print("To update breed's characteristics, choose 4")
    print("\nTo go back, choose b")
    print("To exit the program, choose e\n")

    user_input = input("Selection: ")

    if user_input == "e":
        print("exiting the program...")
        exit()
    
    if user_input == "b":
        print("going back...")
        return user_input
    
    if user_input == "1":
        group = input("Group name: ")

        group_url = check_for_space(group)

        resp = s.get(API_URL + f"/api/groups/{group_url}/")
        body = resp.json()


        response = prompt_from_schema(s, body["@controls"]["edit"])

        if response.status_code == 204:
            print("\nGroup's name successfully updated\n")
            return
        
        else:
            if response.status_code == 409:
                print("Group already exists.")
            else:
                print(f"Error with response code {response.status_code} occurred.")
                print("Try again.")
            put(s)

    if user_input == "2":
        group = input("Group name: ")
        breed = input("Breed name: ")

        group_url = check_for_space(group)
        breed_url = check_for_space(breed)

        resp = s.get(API_URL + f"/api/groups/{group_url}/breeds/{breed_url}")
        if resp.status_code == 404:
            print(f"{breed} in group {group} not found. Try again\n")
            return
        body = resp.json()

        response = prompt_from_schema(s, body["@controls"]["edit"])


        if response.status_code == 204:
            print("\nBreed's name successfully updated\n")
            return
        
        else:
            if response.status_code == 409:
                print("Breed already exists.")
            else:
                print(f"Error with response code {response.status_code} occurred.")
                print("Try again.")
            put(s)
    
    if user_input == "3":
        group = input("Group name: ")
        breed = input("Breed name: ")

        group_url = check_for_space(group)
        breed_url = check_for_space(breed)

        resp = s.get(API_URL + f"/api/groups/{group_url}/breeds/{breed_url}/facts/")
        if resp.status_code == 404:
            print(f"{breed} in group {group} not found. Try again\n")
            return
        body = resp.json()

        facts = {}
        print(f"\nFacts for breed:")
        for item in body["items"]:
            facts[item["fact_id"]] = item["fact"]
            print(item["fact_id"], " - ", item["fact"])

        fact_to_edit = input("Select a fact to edit: ")

        edited_fact = input("Edited fact: ")

        fact_get = s.get(
            API_URL + f"/api/groups/{group_url}/breeds/{breed_url}/facts/{fact_to_edit}/")

        fact_body = fact_get.json()


        response = prompt_from_schema(s, fact_body["@controls"]["edit"],
                                      breed=breed, group=group, model="fact",
                                      fact=fact_to_edit, data=edited_fact)

        if response.status_code == 204:
            print(f"\nFact of breed {breed} successfully updated\n")
            return
        
        else:
            if response.status_code == 409:
                print("Fact already exists.")
            else:
                print(f"Error with response code {response.status_code} occurred.")
                print("Try again.")
            put(s)


    if user_input == "4":
        group = input("Group name: ")
        breed = input("Breed name: ")

        group_url = check_for_space(group)
        breed_url = check_for_space(breed)

        resp = s.get(API_URL + f"/api/groups/{group_url}/breeds/{breed_url}/characteristics/")
        if resp.status_code == 404:
            print(f"{breed} in group {group} not found. Try again\n")
            return
        body = resp.json()

        response = prompt_from_schema(s, body["@controls"]["edit"],
                                      breed=breed, group=group, model="characteristics")


        if response.status_code == 204:
            print(f"\nCharacteristics of breed {breed} successfully updated")
            return
        
        else:
            if response.status_code == 409:
                print("Chars already exists.")
            else:
                print(f"Error with response code {response.status_code} occurred.")
                print("Try again.")
            put(s)
    
    else:
        print("\nInvalid input, try again")
        put(s)

def main_loop():
    with requests.Session() as s:
        while True:
            print("If you want to fetch information, choose 1")
            print("If you want to add information, choose 2")
            print("If you want to update information, choose 3")
            print("If you want to delete information, choose 4")
            print("If you want to exit the application, choose e\n")

            try:
                user_input = input("Selection: ")

                if user_input == "e":
                    print("exiting the program...")
                    exit()

                if user_input == "1":
                    print("you chose to fetch data...")
                    get(s)
                    continue
                
                if user_input == "2":
                    print("you chose to add data...")
                    post(s)
                    continue

                if user_input == "3":
                    print("you chose to update data...")
                    put(s)
                    continue

                if user_input == "4":
                    print("you chose to delete data...")
                    delete(s)
                    continue

                else:
                    print("\nInvalid input, try again\n")

            except TypeError:
                print("Invalid input, try again")
                continue

def main():
    print("\nWelcome to DogDict!\n")
    main_loop()


if __name__ == "__main__":
    main()
    