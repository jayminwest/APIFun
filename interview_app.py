import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

def load_model():
    # unpickle tree.p
    infile = open("tree.p", "rb") # rb is read binary
    header, tree = pickle.load(infile)
    infile.close()
    return header, tree

def tdidt_predict(header, tree, instance):
    info_type = tree[0]
    if info_type == "Leaf":
        return tree[1] # label
    att_index = header.index(tree[1])
    for i in range(2, len(tree)):
        value_list = tree[i]
        if value_list[1] == instance[att_index]:
            return tdidt_predict(header, value_list[2], instance)

# a route is afunction that handles a request
@app.route("/")
def index():
    return "<h1>Welcome to my app</h1>"

@app.route("/predict")
def predict():
    # need to parse the query string to get info for the unseen instance
    level = request.args.get("level")
    lang = request.args.get("lang") 
    tweets = request.args.get("tweets")
    phd = request.args.get("phd")   

    header, tree = load_model()
    pred = tdidt_predict(header, tree, [level, lang, tweets, phd])

    if pred is not None:
        return jsonify({"prediction": pred}), 200
    return "Error making prediction", 400

if __name__ == "__main__":
    header, tree = load_model()
    print(header)
    print(tree)

    app.run(debug=True, port=5000)
    # todo: ste debug=False when deploy