import pickle
import json
import os


# PART A
def read_json(path):
    with open(path) as f:
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

def write_pickle(file_name, source):
    
    outfile = open(file_name, 'wb')  # (wb) write-binary mode
    pickle.dump(source, file_name)
    outfile.close()


# PART D
def load_pickle(pickle_file):
    open(pickle_file, 'rb')  # (rb)read-binary mode
    db = pickle.load(pickle_file)
    for keys in db:
        print(keys, '=>', db[keys])
    pickle_file.close()

'''
read_all_json_files('/Users/jthompson/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/')
write_pickle('/Users/jthompson/dev/PythonFundamentals.Exercises.Part9/data/super_smash_bros/mario.json/')
'''
