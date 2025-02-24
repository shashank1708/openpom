odor_patterns = {
        "alcoholic": Chem.MolFromSmarts("[OX2H]"),  # Hydroxyl group
        "burnt": Chem.MolFromSmarts("[cR1,cR2]"),  # Aromatic carbons (e.g., PAHs)
        "citrus": Chem.MolFromSmarts("C=C(C)C"),  # Limonene-like structure
        "earthy": Chem.MolFromSmarts("[C,O,N]~[C,O,N]~[C,O,N]"),  # General microbial metabolites
        "green": Chem.MolFromSmarts("C=CC[OH]"),  # Unsaturated aldehydes/alcohols
        "mint": Chem.MolFromSmarts("CC(C)C1=CCC(CC1)O"),  # Menthol-l
}