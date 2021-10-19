import time
import json
import requests
from urllib import request
import numpy as np

# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36',
# }

# drugs = np.loadtxt('./source/DTINet/drug.txt', dtype=str)
# for drug in drugs:
#     r = requests.get('https://go.drugbank.com/structures/small_molecule_drugs/{}.pdb'.format(drug), headers=headers)
#     f = open("./data/DTINet/drugs/{}.pdb".format(drug), "w", encoding=r.encoding)
#     for i in r.text: f.write(i)
#     f.close()
#     print(drug)
#     time.sleep(1)

proteins = np.loadtxt('./source/DTINet/protein.txt', dtype=str)
for protein in proteins:
    try:
        r = requests.get('https://www.ebi.ac.uk/proteins/api/proteins/{}'.format(protein))
        content = json.loads(r.text)
        current_db = {}
    except Exception as e:
        print(protein, e)
        continue
    for db in content['dbReferences']:
        if db['type'] != 'PDB': continue
        if 'id' not in db.keys(): continue
        if len(current_db) == 0: 
            current_db = db
            continue

        current_method = current_db['properties']['method']
        properties = db['properties']
        method = properties['method']
        if current_method != method and properties['method'] == 'EM':
            current_db = db
            continue
        
        if 'resolution' not in properties.keys(): continue
        if 'resolution' not in current_db['properties']:
            current_db['properties']['resolution'] = '0.00 A'
        if (current_method != 'EM' and properties['resolution'] >= current_db['properties']['resolution']) \
            or (method == 'EM' and properties['resolution'] >= current_db['properties']['resolution']):
            current_db = db
    if len(current_db) == 0: 
        print(protein, '啥也没有')
        continue
    id = current_db['id']
    try:
        request.urlretrieve('https://files.rcsb.org/download/{}.pdb'.format(id), './data/DTINet/proteins/{}.pdb'.format(protein))
    except Exception as e:
        print(protein, e)
    print(protein, id, current_db['properties']['method'])