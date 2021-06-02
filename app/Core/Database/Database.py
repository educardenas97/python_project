import pickle

class Database():
    def insert(self, object, object_name):
        outfile = open(object_name, 'wb')
        pickle.dump(object, outfile)
        outfile.close()

    def find(self, object_name):
        infile = open(object_name, 'rb')
        response = pickle.load(infile)
        infile.close()
        return response
