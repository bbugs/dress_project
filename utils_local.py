



import json

def load_data0(fname='../data0.json'):
    with open(fname, 'r') as f:
        data0 = json.load(f)

    return data0


def write_line2txt(line, file_object):
    for l in line:
        file_object.write(l, ",")
    pass
