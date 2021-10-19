import os
import numpy as np

drugs = np.loadtxt('./source/DTINet/durg.txt', dtype=str)
proteins = np.loadtxt('./source/DTINet/protein.txt', dtype=str)
for drug in drugs:
    # 加氢报错那咋办呢
    os.system('./pythonsh ./Utilities24/prepare_ligand4.py -l ./data/DTINet/drugs/{}.pdb -U waters -o ./output/{}.pdbqt'.format(drug, drug))
    for protein in proteins:
        print(protein)
        os.system('./pythonsh ./Utilities24/prepare_receptor4.py -r ./data/DTINet/proteins/{}.pdb -U waters -o ./output/{}.pdbqt'.format(protein, protein))

# handler = open("./data/Temp/4X0F.pdbqt", 'r')

# data = []
# while True:
#     line = handler.readline()
#     if not line: break;
#     if line[:4] == "ATOM":
#         line = line[28:55]
#         data.append(line.strip().split())
# data = np.array(data, dtype=float)
# cx, cy, cz = np.around(data.mean(axis=0), 3)
# sx, sy, sz = np.around(np.abs(data.min(axis=0) - data.max(axis=0)))
# print(cx, cy, cz)
# print(sx, sy, sz)

# handler.close()