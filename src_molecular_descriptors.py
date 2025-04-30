from rdkit import Chem  
from rdkit.Chem import Descriptors, AllChem  
  
def calculate_molecular_descriptors(smiles):  
    """Calculate all molecular descriptors used in the analysis"""  
    mol = Chem.MolFromSmiles(smiles)  
    if mol is None:  
        return None  
          
    descriptors = {  
        'MW': Descriptors.ExactMolWt(mol),  
        'LogP': Descriptors.MolLogP(mol),  
        'HBD': Descriptors.NumHDonors(mol),  
        'HBA': Descriptors.NumHAcceptors(mol),  
        'RotBonds': Descriptors.NumRotatableBonds(mol),  
        'TPSA': Descriptors.TPSA(mol),  
        'AromaticRings': Descriptors.NumAromaticRings(mol),  
        'ChiralCenters': len(Chem.FindMolChiralCenters(mol))  
    }  
    return descriptors  