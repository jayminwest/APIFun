
import pickle # a standard python library

# pickle (object serialization): saving a binary representation of an object
# to a file for loading and using later (e.g. a trained model)
# de/unpickle (object de-serialization): loading a binary representation of an
# object from a file into program memory (e.g. a new python process running 
# on a server)

# imagine you just trained a MyDecisionTreeClassifier or a MyRandomForestClassifier
# we are going to pickle it to use it later

interview_header = ["level", "lang", "tweets", "phd"]
interview_tree = ['Attribute', 'level', ['Value', 'Junior', ['Attribute', 'phd', ['Value', 'yes', ['Leaf', 'False', 2, 5]], ['Value', 'no', ['Leaf', 'True', 3, 5]]]], ['Value', 'Mid', ['Leaf', 'True', 4, 14]], ['Value', 'Senior', ['Attribute', 'tweets', ['Value', 'yes', ['Leaf', 'True', 2, 5]], ['Value', 'no', ['Leaf', 'False', 3, 5]]]]]

packaged_obj = (interview_header, interview_tree)
outfile = open("tree.p", "wb")
pickle.dump(packaged_obj, outfile)
outfile.close()