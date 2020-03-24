import pickle
import json
import os


# PART A
def read_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
        return data

# PART B
def read_all_json_files(json_root):
    db_list = []
    
    for root, _, files in os.walk(json_root):
        for f in files:
            if f.endswith('.json'):
                json_content = read_json(os.path.join(json_root, f))
                db_list.append(json_content)
    return db_list


# PART C;

def write_pickle(file_name, data):
    with open(file_name, "wb") as handler:
        pickle.dump(data, handler)


# PART D
def load_pickle(pickle_file):
    with open(pickle_file, 'rb') as handler:
        data = pickle.load(handler)
    return data


'''
read_all_json_files('/Users/jthompson/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/')
write_pickle('super_smash_characters.pickle', '/Users/jthompson/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/mario.json')
load_pickle('/Users/jthompson/dev/PythonFundamentals.Exercises.Part9/super_smash_characters.pickle')
'''

''''
Exercise 2

read_all_json_files('/Users/jthompson/dev/PythonFundamentals.Exercises.Part9/data/ZCW/')
write_pickle('/Users/jthompson/dev/PythonFundamentals.Exercises.Part9/data/ZCW/Data_One.0', 'Data.pickle')
load_pickle('/Users/jthompson/dev/PythonFundamentals.Exercises.Part9/Data.pickle')
'''
