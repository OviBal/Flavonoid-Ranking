import numpy as np  
from rdkit import Chem  
from rdkit.Chem import Descriptors, AllChem  
  
class FAPSCalculator:  
    def __init__(self):  
        self.descriptor_weights = {  
            'MW': -0.0004,  
            'LogP': 0.1444,  
            'HBD': -0.0351,  
            'HBA': -0.0074,  
            'RotBonds': -0.0004,  
            'TPSA': -0.0016,  
            'AromaticRings': 0.0168  
        }  
          
    def calculate_descriptors(self, mol):  
        """Calculate molecular descriptors for FAPS score"""  
        descriptors = {  
            'MW': Descriptors.ExactMolWt(mol),  
            'LogP': Descriptors.MolLogP(mol),  
            'HBD': Descriptors.NumHDonors(mol),  
            'HBA': Descriptors.NumHAcceptors(mol),  
            'RotBonds': Descriptors.NumRotatableBonds(mol),  
            'TPSA': Descriptors.TPSA(mol),  
            'AromaticRings': Descriptors.NumAromaticRings(mol)  
        }  
        return descriptors  
      
    def calculate_faps(self, smiles):  
        """Calculate FAPS score from SMILES string"""  
        mol = Chem.MolFromSmiles(smiles)  
        if mol is None:  
            return None  
              
        descriptors = self.calculate_descriptors(mol)  
        score = sum(value * self.descriptor_weights[key]   
                   for key, value in descriptors.items())  
          
        # Normalize to 0-1 range  
        score = 1 / (1 + np.exp(-score))  
        return score  