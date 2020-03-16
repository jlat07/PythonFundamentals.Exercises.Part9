import pickle
import json
import os


# PART A
def read_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
        return data


# PART B
def read_all_json_files(path):
    db_list = []
    
    for folder in os.listdir(path):
        files = os.path.join(path, folder)
        a = read_json(files)
        db_list.append(eval(json.dumps(a)))
    
    return db_list


# PART C

def write_pickle(data_source_path, output_name):
    db = read_json(data_source_path)
    f = open(output_name, 'wb')  # (wb) write-binary mode
    pickle.dump(db, f)
    f.close()


# PART D
def load_pickle(pickle_file):
    f = open(pickle_file, 'rb')  # (rb)read-binary mode
    a = pickle.load(f)
    db = (eval(json.dumps(a)))
    for keys in db:
        print(keys, '=>', db[keys])
    f.close()


# Part D v2
def loadpickle(filename):
    f = open(filename, 'rb')
    new_dict = pickle.load(f)
    f.close()
    return new_dict


'''
read_all_json_files('/Users/jthompson/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/')
write_pickle('/Users/jthompson/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/mario.json', 'super_smash_characters.pickle')
load_pickle('super_smash_characters.pickle')
'''
