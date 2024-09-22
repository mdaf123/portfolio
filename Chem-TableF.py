soluble_elements = ["NH4", "NO3", "C2H3O2", "CH3COO", "HCO3", "ClO3"]
group1ions = ["Li", "Na", "K", "Rb", "Cs", "Fr"]
grrrr = ["Ag", "Ca", "Sr", "Ba", "Pb"]
while True:
  try:
    x = input("What is your compound(molecular formula)?(Please exlude charges): \n")
    for group1ion in group1ions:
      if group1ion in x:
        print("\n The compound is soluble")
        break
    for polyatomic in soluble_elements:
      if polyatomic in x:
        print("\n The compound is soluble")
        break
    if "Cl" in x or "Br" in x or "I" in x:
      if "Ag" in x or "Pb" in x or "Hg" in x:
        print("\n The compound is insoluble")
      else:
        print("\n The compound is soluble")
    elif "SO4" in x:
      if "Ag" in x or "Pb" in x or "Ba" in x or "Sr" in x or "Ca" in x:
        print("\n The compound is insoluble")
      else:
        print("\n The compound is soluble")
    elif "CO3" in x:
      if "NH4" in x:
        print("\n The compound is soluble")
      else:
        print("\n The compound is insoluble")
    elif "CrO4" in x:
      if "Ca" in x or "Mg" in x or "NH4" in x:
        print("\n The compound is soluble")
      else:
        print("\n The compound is insoluble")
    elif "PO4" in x:
      print("\n The compound is insoluble")
    elif "S" in x:
      print("\n The compound is insoluble")
    elif "OH":
      if "Ca" in x or "Ba" in x or "Sr" in x:
        print("The compound is soluble")
      else:
        print("\n The compound is insoluble")
    break
  except:
    print("Please enter a valid compound")

