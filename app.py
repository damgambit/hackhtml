#!/usr/bin/env python
import os
import random
from flask import Flask, request, jsonify
import numpy as np
import glob
import MySQLdb

import sys
sys.path.insert(0, '/home/damianogambitta/hackhtml')

# default_graph = tf.get_default_graph()

random.seed(0)

   
# initialization
app = Flask(__name__, static_url_path='/static')

import MySQLdb
 
# Connessione al Database
db = MySQLdb.connect("localhost", "root","abc123","hackhtml" )
 
# Ottenimento del cursore
cursor = db.cursor()
 
# Esecuzione di una query SQL
cursor.execute("SELECT VERSION()")
 
# Lettura di una singola riga dei risultati della query
data = cursor.fetchone()
 



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

    # Ottenimento del cursore
    cursor = db.cursor()
     
    # Esecuzione di una query SQL
    cursor.execute("SELECT id_category from category")
     
    # Lettura di una singola riga dei risultati della query
    categories = cursor.fetchall()

    # Ottenimento del cursore
    cursor = db.cursor()
     
    full = []

    for category in categories:
        # Esecuzione di una query SQL
        cursor.execute("SELECT  p.id_product as product_id, p.name, p.path_image as image, \
                c.description as category , MIN(price) as price FROM product as p \
                INNER JOIN category as c on p.id_category = c.id_category\
                      INNER JOIN product_sohp as ps on ps.id_product = p.id_product\
                      WHERE c.id_category = " + str(category[0]) + "\
                      group by p.id_product,p.name,p.path_image,c.description\
            ")
         
        # Lettura di una singola riga dei risultati della query
        data = cursor.fetchall()

        results = []

        for row in data:

            cursor.execute("SELECT s.id_shop, s.address, s.lat, s.lon, s.name\
                    FROM shop as s INNER JOIN product_sohp as ps on s.id_shop = ps.id_shop\
                    WHERE " + str(row[0]) + " = ps.id_product AND ps.price = " + str(row[4]))

            shop = cursor.fetchone()

            shop = {
                'shop_id': shop[0],
                'address': shop[1],
                'lat': shop[2],
                'lon': shop[3],
                'name': shop[4]

            }

            results.append({

                    'product_id': row[0],
                    'name': row[1],
                    'image': row[2],
                    'category': row[3],
                    'price': row[4],
                    'shop': shop


            })

        if results:
            full.append(results)


    # # return the first qt images
    # qt = int(request.args.get('qt'))
    # #get the category
    # category = categories[:qt] 

    # randomize the pants array
    # random.shuffle(category)

    # images = category


    return jsonify({'products':  full})


@app.route('/api/v1/get_similar', methods=['GET'])
def get_similar():
    qt = int(request.args.get('qt'))


    return jsonify({'images': 'ciao'})


if __name__ == '__main__': 
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)