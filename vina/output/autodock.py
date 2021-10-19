import os
# import numpy as np
dti = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
drugs = ['DB00202']

#proteins = np.loadtxt('./source/DTINet/protein.txt', dtype=str)
proteins = ['Q9UI32', 'P00488', 'P35228', 'P06737', 'P11766', 'P50213', 'P30542', 'P00519', 'P12319', 'P00451', 'P23219', 'P35626', 'P21728', 'P35916', 'P51168', 'P02452', 'Q9H4B7', 'P56181', 'P17948', 'Q9UPY5', 'P06213', 'P04049', 'Q9Y285', 'Q9Y234', 'P12259', 'P24530', 'P20309', 'P30613', 'P00734', 'P30273', 'P13716', 'P48167', 'P21554', 'P30556', 'P34995', 'P10515', 'P11836', 'P29475', 'P07195', 'Q07869', 'P51843', 'P10912', 'P00492', 'P28702', 'P12277', 'Q13639', 'P02792', 'P14618', 'Q12809', 'P11229', 'O75380', 'P34972', 'Q15800', 'P11177', 'P17707', 'O76082', 'P13688', 'P51606', 'Q9H244', 'P21673', 'P25021', 'P06746', 'P09622', 'P07741', 'Q05940', 'O95477', 'P17752', 'P03372', 'P08700', 'Q04828', 'P31937', 'P24046', 'P69905', 'P10275', 'P05091', 'P22888', 'P49419', 'P19404', 'P09172', 'Q9Y4W6', 'Q9UHW9', 'P07437', 'P13631', 'P21918', 'Q9H3N8', 'P36888', 'P23368', 'P51649', 'O00180', 'Q9NYK1', 'Q99720', 'P00387', 'O43175', 'Q02218', 'P15692', 'P37288', 'P49916', 'P12532', 'P08588', 'Q9Y5Y9', 'P36021', 'P00367', 'O76074', 'P48637', 'P07814', 'Q8WTV0', 'P37088', 'P14061', 'Q14524', 'Q15046', 'P18858', 'Q13564', 'P30968']
for drug in drugs:
    for i, flag in enumerate(dti):
        protein = proteins[i]
        print(protein)
        os.system('../pythonsh ../Utilities24/prepare_dpf4.py -l ./{ligand}.pdbqt -r ./{receptor}.pdbqt -o ./{ligand}_{receptor}.dpf'.format_map({'ligand': drug, 'receptor': protein}))
        os.system('../pythonsh ../Utilities24/prepare_gpf4.py -l ./{ligand}.pdbqt -r ./{receptor}.pdbqt -o ./{ligand}_{receptor}.gpf'.format_map({'ligand': drug, 'receptor': protein}))

        os.system('./autogrid4 -p ./{}_{}.gpf'.format(drug, protein))
        os.system('./autodock4 -p ./{}_{}.dpf'.format(drug, protein))
        os.system(r"egrep 'Estimated Free Energy of Binding' {ligand}_{receptor}.dlg | awk -F ' ' '{{print $(NF-2)}}' >> mbe_{ligand}_{receptor}.txt".format_map({'ligand': drug, 'receptor': protein}))
