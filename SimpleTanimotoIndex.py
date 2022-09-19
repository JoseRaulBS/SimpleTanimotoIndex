from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator
from rdkit import DataStructs

rdkit_gen = rdFingerprintGenerator.GetRDKitFPGenerator(maxPath=7)

molecule1_name = "THC"
molecule1_smile = "CCCCCc1cc(c2c(c1)OC([C@H]3[C@H]2C=C(CC3)C)(C)C)O"

molecule2_name = "CBD"
molecule2_smile = "CCCCCc1cc(c(c(c1)O)[C@@H]2C=C(CC[C@H]2C(=C)C)C)O"

def simple_tanimoto(name1, smiles1, name2, smiles2):
    a = Chem.MolFromSmiles(smiles1)
    b = Chem.MolFromSmiles(smiles2)
    a2= rdkit_gen.GetFingerprint(a)
    b2= rdkit_gen.GetFingerprint(b)

    similarity = DataStructs.TanimotoSimilarity(a2, b2)
    similarity = round(similarityJR,3)
    print(f"\nTanimoto coefficient:\n "
          f"{name1} vs {name2} -> {similarity}")
    return


simple_tanimoto(molecule1_name, molecule1_smile,
            molecule2_name, molecule2_smile)
