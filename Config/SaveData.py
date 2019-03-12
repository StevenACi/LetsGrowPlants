from Logs import log
import json

__config_file_address = "../Config/"


def get_json(filename):
    config = None
    try:
        with open(__config_file_address + filename + ".json") as jsonfile:
            config = json.load(jsonfile)
    except FileNotFoundError:
        log.ERROR("File " + __config_file_address + filename + ".json not found.")
    return config


def save_json(data, saveFile):
    try:
        with open(__config_file_address + saveFile+'.json', 'w') as outfile:
            json.dump(data, outfile)
    except FileNotFoundError:
        log.ERROR("File " + __config_file_address + saveFile + ".json not found.")


def save(plant):
    root = {'vite': 0, 'waterPP': 0, 'waterDrain': 0, 'length': 0, 'growF': 0, 'isDead': False,
            'children': [], 'upkeepMet': True}

    currentData = {"roots": {}, "rootchildren": {}}
    root = []
    rootclone = plant.roots
    child = []
    childclone = rootclone[0].children

    for rIndex, rr in enumerate(rootclone):
        root.append(rr.__dict__)

    for ch in childclone:
        child.append(ch.__dict__)

    currentData["roots"] = root
    currentData["rootchildren"] = child
    print(currentData)
    # SaveData.save_json(currentData, "save")
