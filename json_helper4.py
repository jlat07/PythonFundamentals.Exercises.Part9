#PART C

def write_pickle():
    data = []
    file = open('link.json', 'wb')  # (wb) write-binary mode
    pickle.dump(data, file)
    file.close()


write_pickle()


# PART D
def load_pickle():
    file = open('*.pickle', 'rb')  # (rb)read-binary mode
    data = pickle.load(file)
    file.close()
    print("pickled data: ")

    cnt = 0
    for item in data:
        print(cnt, " = ", item)
        cnt += 1


load_pickle()