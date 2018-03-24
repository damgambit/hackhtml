#!/usr/bin/env python
import os
import random
from flask import Flask, request, jsonify
import numpy as np
import glob
import MySQLdb


# default_graph = tf.get_default_graph()

random.seed(0)

   
# initialization
app = Flask(__name__, static_url_path='/static')



def get_links(path):
    return [link.replace('./', '/') for link in glob.glob(path + "*")]

camicie = get_links('./static/dataset/camicie/')
cappelli = get_links('./static/dataset/cappelli/')
maglioni_mad = get_links('./static/dataset/maglioni_mad/')
pantaloni = get_links('./static/dataset/pantaloni/')
patches = get_links('./static/dataset/patches/')
scarpe_adidas = get_links('./static/dataset/scarpe_adidas/')
skateboard = get_links('./static/dataset/skateboard/')
tshirt_heart = get_links('./static/dataset/tshirt_heart/')
zaini = get_links('./static/dataset/zaini/')

print(camicie)


categories = [

    cappelli,
    maglioni_mad,
    pantaloni,
    patches,
    scarpe_adidas,
    skateboard,
    tshirt_heart,
    zaini,

]

categories = []

i = 0

products = []
for item in camicie:
    products.append({
        'id': i,
        'image': item
    })
    i += 1
    categories.append(products)

products = []
for item in maglioni_mad:
    products.append({
        'id': i,
        'image': item
    })
    i += 1
    categories.append(products)

products = []
for item in patches:
    products.append({
        'id': i,
        'image': item
    })
    i += 1
    categories.append(products)

products = []
for item in pantaloni:
    products.append({
        'id': i,
        'image': item
    })
    i += 1
    categories.append(products)

products = []
for item in scarpe_adidas:
    products.append({
        'id': i,
        'image': item
    })
    i += 1
    categories.append(products)


products = []
for item in skateboard:
    products.append({
        'id': i,
        'image': item
    })
    i += 1
    categories.append(products)


products = []
for item in tshirt_heart:
    products.append({
        'id': i,
        'image': item
    })
    i += 1
    categories.append(products)


products = []
for item in zaini:
    products.append({
        'id': i,
        'image': item
    })
    i += 1
    categories.append(products)




@app.route('/api/v1/products', methods=['GET'])
def get_category():
    # SELECT * FROM table ORDER BY RAND() LIMIT 1


    #randomize the categories
    # random.shuffle(products)

    # return the first qt images
    qt = int(request.args.get('qt'))
    #get the category
    category = categories[:qt] 

    # randomize the pants array
    # random.shuffle(category)


    

    images = category


    return jsonify({'products':  images})


@app.route('/api/v1/get_similar', methods=['GET'])
def get_similar():
    qt = int(request.args.get('qt'))


    return jsonify({'images': 'ciao'})


if __name__ == '__main__': 
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)