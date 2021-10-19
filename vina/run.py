import numpy as np

dti = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
drugs = ['DB00050']

proteins = np.loadtxt('./source/DTINet/protein.txt', dtype=str)
for drug in drugs:
    #exec('pythonsh ../../Utilities24/prepare_receptor4.py -r ./{}.pdb -A hydrogens -U waters -o ')
    for i, flag in enumerate(dti):
        print(proteins[i])

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