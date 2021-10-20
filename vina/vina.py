import os
import numpy as np

drug_ignore = True
drug_point = 'DB00050'
drugs = np.loadtxt('./source/DTINet/drug.txt', dtype=str)
proteins = np.loadtxt('./source/DTINet/protein.txt', dtype=str)
for drug in drugs:
    if drug == drug_point: drug_ignore = False
    if drug_ignore: continue
    # 加氢报错那咋办呢
    os.system('./pythonsh ./Utilities24/prepare_ligand4.py -l ./data/DTINet/drugs/{}.pdb -U waters -o ./output/{}.pdbqt'.format(drug, drug))


    protein_ignore = True
    protein_point = 'P00488'
    for protein in proteins:
        if protein == protein_point: protein_ignore = False
        if protein_ignore: continue

        os.system('./pythonsh ./Utilities24/prepare_receptor4.py -r ./data/DTINet/proteins/{}.pdb -U waters -o ./output/{}.pdbqt'.format(protein, protein))

        if not os.path.exists("./output/{}.pdbqt".format(protein)): continue
        handler = open("./output/{}.pdbqt".format(protein), 'r')
        data = []
        while True:
            line = handler.readline()
            if not line: break
            if line[:4] == "ATOM":
                flag = line.index(line.split()[5])
                item = [line[-50:-42].strip(), line[-42:-34].strip(), line[-34:-26].strip()]
                data.append(item)
        data = np.array(data, dtype=float)
        cx, cy, cz = np.around(data.mean(axis=0), 3)
        sx, sy, sz = np.around(np.abs(data.min(axis=0) - data.max(axis=0)))
        handler.close()
        print(drug, protein, cx, cy, cz)

        params = {
            'receptor': protein,
            'ligand': drug,
            'cx': cx,
            'cy': cy,
            'cz': cz,
            'sx': sx,
            'sy': sy,
            'sz': sz,
        }
        
        os.system('./vina --receptor ./output/{receptor}.pdbqt --ligand ./output/{ligand}.pdbqt --exhaustiveness 30 --center_x {cx} --center_y {cy} --center_z {cz} --size_x {sx} --size_y {sy} --size_z {sz} --log ./output/vina/{ligand}_{receptor}.txt'.format_map(params))