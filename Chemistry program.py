    #combined gas law
def combined_gas_formula():
      q=""
      while q not in [0,1,2,3,4,5]:
        print("Please choose the following: \n \n 1. What is p1? \n 2. What is p2? \n 3. What is v1? \n 4. What is v2? \n 5. What is t1? \n 6. What is t2? \n")
        q=int(input("What is your question?, Please choose from 1-6: \n \n").lower().strip())
        q=q-1
        if q not in [0,1,2,3,4,5]:
          print("Please choose from 1-6 \n")
          print("Please choose the following: \n \n 1. What is p1? \n 2. What is p2? \n 3. What is v1? \n 4. What is v2? \n 5. What is t1? \n 6. What is t2? \n")
      if q==0:
        w=input("What is the value of P2?: ")
        while w.isnumeric()==False:
          w=input("What is the value of P2?: ")
        w=float(w)
        e=input("What is the value of V2?: ")
        while e.isnumeric()==False:
          e=input("What is the value of V2?: ")
        e=float(e)
        r=input("What is the value of V1?: ")
        while r.isnumeric()==False:
          r=input("What is the value of V1?: ")
        r=float(r)
        t=input("What is the value of T1?: ")
        while t.isnumeric()==False:
          t=input("What is the value of T1?: ")
        t=float(t)
        y=input("What is the value of T2?: ")
        while y.isnumeric()==False:
          y=input("What is the value of T2?: ")
        y=float(y)
        print("\n p1 =", ((w*e*t)/(r*y)))
      if q==1:
        w=input("What is the value of P1?: ")
        while w.isnumeric() == False:
         w=input("What is the value of P1?: ")
        w=float(w)
        e=input("What is the value of V2?: ")
        while e.isnumeric()==False:
          e=input("What is the value of V2?: ")
        e=float(e)
        r=input("What is the value of V1?: ")
        while r.isnumeric()==False:
          r=input("What is the value of V1?: ")
        r=float(r)
        t=input("What is the value of T1?: ")
        while t.isnumeric()==False:
          t=input("What is the value of T1?: ")
        t=float(t)
        y=input("What is the value of T2?: ")
        while y.isnumeric()==False:
          y=input("What is the value of T2?: ")
        y=float(y)
        print("\n P2 =", ((w*r*y)/(e*t)))
      if q==2:
        w=input("What is the value of P2?: ")
        while w.isnumeric()==False:
          w=input("What is the value of P2?: ")
        w=float(w)
        e=input("What is the value of P1?: ")
        e=input("What is the value of P1?: ")
        while e.isnumeric() == False:
         e=input("What is the value of P1?: ")
        e=float(e)
        r=input("What is the value of V2?: ")
        while r.isnumeric()==False:
          r=input("What is the value of V2?: ")
        r=float(r)
        t=input("What is the value of T1?: ")
        while t.isnumeric()==False:
          t=input("What is the value of T1?: ")
        t=float(t)
        y=input("What is the value of T2?: ")
        while y.isnumeric()==False:
          y=input("What is the value of T2?: ")
        y=float(y)
        print("\n V1 =", ((w*r*t)/(e*y)))
      if q==3:
        w=input("What is the value of P1?: ")
        while w.isnumeric() == False:
          w=input("What is the value of P1?: ")
        w=float(w)
        e=input("What is the value of V1?: ")
        while e.isnumeric()==False:
          e=input("What is the value of V1?: ")
        e=float(e)
        r=input("What is the value of P2?: ")
        while r.isnumeric()==False:
          r=input("What is the value of P2?: ")
        r=float(r)
        t=input("What is the value of T2?: ")
        while t.isnumeric()==False:
          t=input("What is the value of T2?: ")
        t=float(t)
        y=input("What is the value of T1?: ")
        while y.isnumeric()==False:
          y=input("What is the value of T1?: ")
        y=float(y)
        print("\n V2 =", ((w*e*t)/(r*y)))
      if q==4:
        w=input("What is the value of P1?: ")
        while w.isnumeric() == False:
           w=input("What is the value of P1?: ")
        w=float(w)
        e=input("What is the value of V1?: ")
        while e.isnumeric()==False:
          e=input("What is the value of V1?: ")
        e=float(e)
        r=input("What is the value of V2?: ")
        while r.isnumeric()==False:
          r=input("What is the value of V2?: ")
        r=float(r)
        t=input("What is the value of P2?: ")
        while t.isnumeric()==False:
          t=input("What is the value of P2?: ")
        t=float(t)
        y=input("What is the value of T2?: ")
        while y.isnumeric()==False:
          y=input("What is the value of T2?: ")
        y=float(y)
        print("\n T1 =", ((w*e*y)/(r*t)))
      if q==5:
        w=input("What is the value of T1?: ")
        while w.isnumeric() == False:
          w=input("What is the value of T1?: ")
        w=float(w)
        e=input("What is the value of V1?: ")
        while e.isnumeric()==False:
          e=input("What is the value of V1?: ")
        e=float(e)
        r=input("What is the value of V2?: ")
        while r.isnumeric()==False:
          r=input("What is the value of V2?: ")
        r=float(r)
        t=input("What is the value of P1?: ")
        while t.isnumeric()==False:
          t=input("What is the value of P1?: ")
        t=float(t)
        y=input("What is the value of T2?: ")
        while y.isnumeric()==False:
          y=input("What is the value of T2?: ")
        y=float(y)
        print("\n T2 =", ((w*r*y)/(e*t)))
    #acids and bases determiner
def acids_bases():
      a=""
      while a not in ["yes", "no"]:
        a = input("Would you like to use our acid base determiner: \n \n ")
        if a == "yes":
          print("\n oki doki \n")
          b=""
          while b not in ["yes", "no"]:
            b = input("Do you have the pH of your solution? \n \n ")
            if b == "yes":
              while True:
                try:
                  c = input("What is the pH of your solution? \n\n")
                  if 14 >= float(c) > 7 :
                    print("\n Your solution is basic")
                    break
                  elif 0 < float(c) < 7:
                    print("\n Your solution is acidic")
                    break
                  elif float(c) == 7:
                    print("\n Your solution is neutral")
                    break
                  else:
                    print("")
                    print("Please enter a valid number")
                    print("")
                except ValueError:
                  print("")
                  print("Goon off!")
                  print("")
            if b not in ["yes", "no"]:
              print("")
              print("Please enter a valid answer, either 'yes' or 'no'")
              print("")
            if b == "no":
              print("")
              q=""
              while q not in ["yes", "no"]:
                q=input("Do you know the pOH of your solution? \n \n ")
                if q == "yes":
                  print("")
                  while True:
                    try:
                      d = input("What is the pOH of your solution? \n \n ")
                      if 0.0 < float(d) < 7.0:
                        print("")
                        print("Your solution is basic")
                        break 
                      elif 14.0 >= float(d) > 7.0:
                        print("")
                        print("Your solution is acidic")
                        break
                      elif float(d) == 7.0:
                        print("")
                        print("Your solution is neutral")
                        break
                      else:
                        print("")
                        print("Please enter a valid number")
                        print("")
                    except ValueError:
                      print("")
                      print("Goon off!")
                      print("")
                if q not in ["yes", "no"]:
                  print("")
                  print("This is a yes or no question you goober! \n \n ")
                if q == "no":
                  print("")
                  w=""
                  while w not in ["yes", "no"]:
                    w = input("\n Do you have an indicator? \n \n ")
                    if w == "yes":
                      print("")
                      p=""
                      List=["methyl orange", "litmus", "litmus paper", "bromthymol blue", "phenolphthalein", "bromcresol green", "thymol blue"]
                      while p not in List:
                        p = input("What is the indicator? \n \n ").lower().strip()                  
                        if p == "litmus" or p == "litmus paper":
                          print("")
                          litmus_color=""
                          while litmus_color not in ["red", "blue"]:
                            litmus_color = input("\n What color is the indicator? \n \n ").lower()
                            if litmus_color == "red":
                               print("")
                               print("Your solution is acidic")
                            elif litmus_color == "blue":
                                print("")
                                print("Your solution is basic")
                            else:
                              print("")
                              print("Give me a valid answer, you goober!!")   
                              print("")
                        elif p == "bromcresol green":
                          print("")
                          bg_color=""
                          while bg_color not in ["yellow", "green"]:
                            bg_color = input("\n What color is the indicator? \n \n ").lower()
                            if bg_color == "yellow":
                              print("")
                              print("Your solution is acidic")
                            elif bg_color == "green":
                              print("")
                              print("Sorry can't help you!")
                            else:
                              print("")
                              print("Give me a valid answer, you goober!!")
                        elif p == "bromthymol blue":
                          print("")
                          bromthymol=""
                          while bromthymol not in ["yellow", "blue"]:
                            bromthymol = input("\n What color is the indicator? \n \n ").lower()
                            if bromthymol == "yellow":
                              print("")
                              print("Your solution is acidic")
                            elif bromthymol == "blue":
                              print("")
                              print("Your solution is basic")
                            else:
                              print("")
                              print("Give me a valid answer, you goober!! \n")                    
                        elif p == "methyl orange":
                          print("")
                          methyl=""
                          while methyl not in ["yellow", "orange", "red"]:
                            methyl = input("What color is the indicator? \n \n ").lower()
                            if methyl == "yellow":
                              print("")
                              print("Sorry can't help you!")
                            elif methyl in ["red", "orange"]:
                              print("")
                              print("Your solution is acidic")
                            else:
                              print("")
                              print("Give me a valid answer you blind ape you ratchet chimp!")
                        elif p == "phenolphthalein":
                          print("")
                          phent=""
                          while phent not in ["colorless", "pink"]:
                            phent=input("What color is the indicator? \n \n ").lower()
                            if phent == "colorless":
                              print("\n Sorry can't help you!")
                            elif phent == "pink":
                              print("")
                              print("Your solution is basic")
                            else:
                              print("\n Don't make me smack you now!")
                              print("")
                        elif p == "thymol blue":
                          print("")
                          thymol=""
                          while thymol not in ["blue", "yellow"]:
                            thymol = input("What color is the indicator? \n \n ")
                            if thymol == "blue":
                              print("\n Your solution is basic")
                            elif thymol == "yellow":
                              print("\n Sorry can't help you!")
                            else:
                              print("That's it, Ima smack the skibidi out you! \n")
                        else:
                          print("")
                          print("Please enter a valid indicator \n")
                    elif w == "no" :
                     print("")
                     print("fuck outta here you bum")
                     print("")
        if a not in ["yes", "no"]:
          print("")
          print("Please enter yes or no")
          print("")
        if a == "no":
          print("")
          print("Get the damn outta here")
    #arhennius
def arhennius():
      q=""
      while q not in ["oh", "h", "h+", "oh-", "hydroxide", "hydrogen", "hydrogen+", "hydrogen ion", "proton"]:
        q=input("Which ion does the compound contain?: \n \n").lower()
        if q in ["oh", "oh-", "hydroxide"]:
          print("\n The compound is an arhennius base")
        elif q in ["h", "h+", "hydrogen", "hydrogen+", "hydrogen ion", "proton"]:
          print("\n The compound is an arhennius acid")
        else:
          print("\n Please enter a valid input \n")
    #sigfigs
def sigfigs():
      x = input("Type your number completely: \n \n")
      list_x = []
      for i in x:
        list_x.append(i)
      try:
        list_x.remove(".")
        while list_x[0] == "0":
          list_x.remove(list_x[0])
      except:
        while list_x[0] == "0":
          list_x.remove(list_x[0])
        while list_x[-1] == "0":
          list_x.remove(list_x[-1])
      print(f"Your number has {len(list_x)} significant figures.")
      return
def organic_groups():
      while True:
        while True:
          q = input("\nWhat is your organic compound?: \n\n").lower().strip()
          if "c" not in q or "h" not in q:
            print("\nGet out!")
          else:
            break
        halide_ions = ["f", "cl", "br", "i"]
        for halide in halide_ions:
          if halide in q:
            print("\n This is a halide")
            break
        if "oh" in q and "ooh" not in q:
          while True:
            try:
              monkeyman=0
              for char in q:       
                if char == "2":
                  monkeyman = monkeyman+1
                  a=q.find("2")
                  q = q[:a] + "l" +q[a+1:]
                elif "2" not in q:
                  break
              break
            except(ValueError):
              break
          e=q.find("o")
          if e == a+1:
            print("\n This is an alcohol")
            break
          elif e != a+1:
            print("\n This is an aldehyde")
            break
        elif "ooh" in q:
          print("\n This is an organic(carboxylic) acid")
          break
        elif "n" in q:
          if "o" in q:
            print("\n This is an amide")
            break
          else:
            print("\n This is an amine")
            break
        elif "oo" in q:
          print("\n This is an ester")
          break
        elif "o" in q:
          a = float(q[1])
          b = float(q[3])
          if b == (a*2):
            print("\n This is a ketone")
            break
          else:
            print("\n This is an ether")
            break
        else:
          print("\n I am afraid that you seem to be mistaken")
def polarity():
      nonmetal = ["h", "he", "c", "n", "o", "f", "ne", "p", "s", "cl", "ar", "se", "br", "kr", "i", "xe", "rn", "og", "hydrogen", "helium", "carbon", "nitrogen", "oxygen", "fluorine", "neon", "phosphorus", "sulfur", "chlorine", "argon", "selenium", "bromine", "krypton", "iodine", "xenon", "radon", "oganesson"
                 ]     
      metal = ["li", "be", "na", "mg", "al", "k", "ca", "sc", "ti", "v", "cr", "mn", "fe", "co", "ni", "cu", "zn", "ga", "rb", "sr", "y", "zr", "nb", "mo", "tc", "ru", "rh", "pd", "ag", "cd", "in", "sn", "cs", "ba", "la", "ce", "pr", "nd", "pm", "sm", "eu", "gd", "tb", "dy", "ho", "er", "tm", "yb", "lu", "hf", "ta", "w", "re", "os", "ir", "pt", "au", "hg", "tl", "pb", "bi", "po", "fr", "ra", "ac", "th", "pa", "u", "np", "pu", "am", "cm", "bk", "cf", "es", "fm", "md", "no", "lr", "rf", "db", "sg", "bh", "hs", "mt", "ds", "rg", "cn", "nh", "fl", "mc", "lv", "ts", "lithium", "beryllium", "sodium", "magnesium", "aluminum", "potassium", "calcium", "scandium", "titanium", "vanadium", "chromium", "manganese", "iron", "cobalt", "nickel", "copper", "zinc", "gallium", "rubidium", "strontium", "yttrium", "zirconium", "niobium", "molybdenum", "technetium", "ruthenium", "rhodium", "palladium", "silver", "cadmium", "indium", "tin", "cesium", "barium", "lanthanum", "cerium", "praseodymium", "neodymium", "promethium", "samarium", "europium", "gadolinium", "terbium", "dysprosium", "holmium", "erbium", "thulium", "ytterbium", "lutetium", "hafnium", "tantalum", "tungsten", "rhenium", "osmium", "iridium", "platinum", "gold", "mercury", "thallium", "lead", "bismuth", "polonium", "francium", "radium", "actinium", "thorium", "protactinium", "uranium", "neptunium", "plutonium", "americium", "curium", "berkelium", "californium", "einsteinium", "fermium", "mendelevium", "nobelium", "lawrencium", "rutherfordium", "dubnium", "seaborgium", "bohrium", "hassium", "meitnerium", "darmstadtium", "roentgenium", "copernicium", "nihonium", "flerovium", "moscovium", "livermorium", "tennessine"
              ]
      polyatomic_ions = [
          "ammonium", "nh4",
          "acetate", "c2h3o2",
          "carbonate", "co3",
          "hydrogen carbonate (bicarbonate)", "hco3",
          "hydroxide", "oh",
          "nitrate", "no3",
          "nitrite", "no2",
          "phosphate", "po4",
          "hydrogen phosphate", "hpo4",
          "dihydrogen phosphate", "h2po4",
          "sulfate", "so4",
          "hydrogen sulfate (bisulfate)", "hso4",
          "sulfite", "so3",
          "hydrogen sulfite (bisulfite)", "hso3",
          "chromate", "cro4",
          "dichromate", "cr2o7",
          "peroxide", "o2",
          "permanganate", "mno4",
          "cyanide", "cn",
          "thiocyanate", "scn",
          "oxalate", "c2o4"
      ]
      def binary():
        while True:
          x = input("\n What is the first element of your compound?: \n \n").lower().strip()
          y = input("\n What is the second element of your compound: \n \n").lower().strip()
          if x in metal and y in metal:
            print("\n Your compound is metallic")
            break
          elif x in nonmetal and y in nonmetal:
            if x == "h" or x == "hydrogen":
              b = 2.2
            elif x == "c" or x == "carbon":
              b = 2.6
            elif x == "n" or x == "nitrogen":
              b = 3.0
            elif x == "o" or x == "oxygen":
              b = 3.4
            elif x == "f" or x == "fluorine":
              b = 4.0
            elif x == "p" or x == "phosphorus":
              b = 2.2
            elif x == "s" or x == "sulfur":
              b = 2.6
            elif x == "cl" or x == "chlorine":
              b = 3.2
            elif x == "se" or x == "selenium":
              b = 2.6
            elif x == "br" or x == "bromine":
              b = 3.0
            elif x == "i" or x == "iodine":
              b = 2.7
            elif x == "xe" or x == "xenon":
              b = 2.6
            if y == "h" or y == "hydrogen":
              a = 2.2
            elif y == "c" or y == "carbon":
              a = 2.6
            elif y == "n" or y == "nitrogen":
              a = 3.0
            elif y == "o" or y == "oxygen":
              a = 3.4
            elif y == "f" or y == "fluorine":
              a = 4.0
            elif y == "p" or y == "phosphorus":
              a = 2.2
            elif y == "s" or y == "sulfur":
              a = 2.6
            elif y == "cl" or y == "chlorine":
              a = 3.2
            elif y == "se" or y == "selenium":
              a = 2.6
            elif y == "br" or y == "bromine":
              a = 3.0
            elif y == "i" or y == "iodine":
              a = 2.7
            elif y == "xe" or y == "xenon":
              a = 2.6
            z = abs(b-a)                
            if z>0.4:
              print("\n Your compound is polar-covalent")
            elif z<0.4 or z==0.4:
              print("\n Your compound is non-polar-covalent")
          elif x in metal and y in nonmetal:
            while len(x) == 2:
              x = x.capitalize()
              break
            while len(y) == 2:
              y = y.capitalize()
              break
            print(f"\n {x}{y} compound is an ionic compound")
            break
          else:
            print("\n GOOBER! \n")
            continue
      def tertiary():
        print()
        y_n = input("Would you like table E printed here? (y/n): \n \n").strip().lower()
        while y_n not in ["y", "n", "yes", "no"]:
          print("Please respond with 'y' or 'n'")
          y_n = input("Would you like table E printed here? (y/n): \n")
        if y_n in ["y", "yes"]:
          print(polyatomic_ions)
        elif y_n in ["n", "no"]:
          print("\n Okie dokie \n")
        else:
          print()
          syntaxif = input("Do you see  (y/n): \n \n").strip().lower()   
        qualoppy = input("""What is the entire formula of your compound,\n  *barring any parentheticals and charges?: \n \n""").lower().strip()
        def remove_numbers(input_string):
          result = ""
          for char in input_string:
              if not char.isdigit():
                  result += char
          return result
        def declog(com_len, com):
          if com_len == 4:
              sub1 = com[0] + com[1]
              sub2 = com[2] + com[3]  
              return sub1, sub2
          elif com_len == 3:
              sub1 = com[0] 
              sub2 = com[1] + com[2]
              return sub1, sub2
          else:
            return ''
        polyion_special = [
            "nh",
            "cho",
            "co",
            "hco",
            "no",
            "no",
            "so",
            "hso",
            "so",
            "po",
            "hpo",
            "hpo",
            "clo",
            "clo",
            "clo",
            "clo",
            "mno",
            "cro",
            "cro",
            "co",
            "cn",
            "scn",
            "hg"
        ]
        c = 0
        d = 0
        if "po4" in qualoppy or "po3" in qualoppy or "co3" in qualoppy or "no2" in qualoppy or "no3" in qualoppy:
          print("It would appear that your compound contains one of the following polyatomic ions\n\n: PO4, PO3, CO3, NO2, NO3")

          while True:
            a = input("Please re-enter the other chemical symbol(s) found in the formula: ").strip().lower()

            # Remove numeric characters from the input string
            cleaned_input = ''.join(char for char in a if not char.isdigit())

            # Check if cleaned input is in metals
            if cleaned_input in metal:
                return print("Your compound is ionic")
                break
            else:
                return print("Your compound is covalent")
                break
        for i in polyatomic_ions:
          if i.lower() in qualoppy:
            d += 1
        if d != 0:

          bred = ""
          for i in qualoppy:
            if i.isnumeric() == True:
              i.replace(i, '')
            elif i == " ":
              i.replace(i, '')
            elif i == "(":
              i.replace(i, '')
            elif i == ")":
              i.replace(i, '')
            else:
              bred += i

          cow = 0
          a = (declog(len(bred), bred))

          for i in a:

            if i.lower() in metal:
              cow = cow - 1

            elif i.lower() in nonmetal or polyion_special:
              cow = cow + 1

          if cow == len(a):
            return print("Your compound is covalent")
          elif cow != len(a):
            for i in a:
              if i.lower() in metal:
                return print("Your compound is ionic")
          else:
            return print("An unexpected error has occured")
      print("""Binary compounds are marked by two elements \n      i.e: H2O, CO2, NH3, etc. \nTertiary compounds contain three elements \n *and sometimes have a parenthetical \n\n      i.e: H2SO4, Ca(OH)2, H3PO4  etc. \n """)
      qualop = "eskew"
      while qualop not in ["binary", "tertiary"]:
        qualop = input("Is your compound binary or tertiary?:\n").strip().lower()
        if qualop == "binary":
          print()
          binary()
        elif qualop == "tertiary":
          print()
          tertiary()
        else:
          print("\nPlease enter a valid option(binary or tertiary) \n")
def alkynes_alkenes_alkanes():
      def Table_Q():
        while True:
          try:
            x = input("\n Write down the molecular formula of your compound: \n\n").lower().strip()
            w = float(x[1])
            z = float(x[3])
            if z == (2*w)+2:
              print("\n This is an alkane")
              q = "ane"
            elif z == 2*w:
              print("\n This is an alkene")
              q = "ene"
            elif z == (2*w)-2:
              print("\n This is an alkyne")
              q = "yne"
            if w == 2:
              e = "eth"
            elif w == 3:
              e = "prop"
            elif w == 4:
              e = "but"
            elif w == 5:
              e = "pent"
            elif w == 6:
              e = "hex"
            elif w == 7:
              e = "hept"
            elif w == 8:
              e = "oct"
            elif w == 9:
              e = "non"
            elif w == 10:
              e = "dec"
            print("\n The name of your compound is "+e+q)
            break
          except(ValueError, TypeError):
            print("\n Blithering idiot \n")
      def Name_Diagnosis():
        q = input("What is the name of your hydrocarbon?: ").strip().lower()
        while q.isnumeric() == True:
          print("Please write down the name of your hydrocarbon\n barring any hypens or coefficients")
          q = input("What is the name of your hydrocarbon?: ").lower().strip()
        now = list(q)
        nower = []
        c = 0
        for i in range(1,4):
          c += -1
          nower.append(now[c])
        if nower[-3] == "s":
          nower.pop(-3)
          nower.append(now[-4])
        The_w = "".join(nower) 
        The_z = list(reversed(The_w))
        The_W2 = "".join(The_z)
        if The_W2 == "ane":
          return print(f"The hydrocarbon {q} is an alkane")
        elif The_W2 == "ene":
          return print(f"The hydrocarbon {q} is an alkene") 
        elif The_W2 == "yne":
          return print(f"The hydrocarbon {q} is an alkyne")
        else:
          return print(f"The compound {q} is not a nyc regents hydrocarbon")
      Name_Diagnosis()
      baby_gronk = input("Do you have the molecular formula of your compound or name?(Say mf for molecular formular; say n for name): \n\n").lower().strip()
      if baby_gronk == "mf":
        Table_Q()
      elif baby_gronk == "n":
        Name_Diagnosis()
def percent_comp():
      while True:
        try:
          x = float(input("\nWhat is the mass of the element? \n If you don't know say idk: \n\n"))
          y = float(input("\nWhat is the total mass of the compound?: \n\n"))
          print(f"\nThe percent composition is {x/y*100}%")
          break
        except(ValueError, TypeError):
          q = ""
          while q not in ["yes", "no"]:
            q = input("\nDo you know how many moles of the element are in the compound?: \n\n").lower().strip()
            if q == "yes":
              while True:
                try:
                  z = float(input("\nHow many moles of the element are in the compound?: \n\n"))
                  e = float(input("\nWhat is the gfm(if you don't know you can use one of our other functions that determine gfm) of the element(Don't state the unit just the number)?: \n\n"))
                  r = float(input("\nWhat is the gfm of the compound?: \n\n"))
                  print("The percent composition is", z*e/r*100, "%\n")
                  break
                except(ValueError, TypeError):
                  print("You goon!\n")
              break
            elif q == "no":
              print("Sorry can't help ya\n")
              break
          break
def gfm():
      atomic_masses = {
        'H': 1.008, 'He': 4.0026, 'Li': 6.94, 'Be': 9.0122, 'B': 10.81, 'C': 12.01, 'N': 14.01, 'O': 16.00,
        'F': 19.00, 'Ne': 20.18, 'Na': 22.99, 'Mg': 24.31, 'Al': 26.98, 'Si': 28.09, 'P': 30.97, 'S': 32.07,
        'Cl': 35.45, 'K': 39.10, 'Ar': 39.95, 'Ca': 40.08, 'Sc': 44.96, 'Ti': 47.87, 'V': 50.94, 'Cr': 52.00,
        'Mn': 54.94, 'Fe': 55.85, 'Ni': 58.69, 'Co': 58.93, 'Cu': 63.55, 'Zn': 65.38, 'Ga': 69.72, 'Ge': 72.63,
        'As': 74.92, 'Se': 78.96, 'Br': 79.90, 'Kr': 83.80, 'Rb': 85.47, 'Sr': 87.62, 'Y': 88.91, 'Zr': 91.22,
        'Nb': 92.91, 'Mo': 95.95, 'Tc': 98.00, 'Ru': 101.1, 'Rh': 102.9, 'Pd': 106.4, 'Ag': 107.9, 'Cd': 112.4,
        'In': 114.8, 'Sn': 118.7, 'Sb': 121.8, 'I': 126.9, 'Te': 127.6, 'Xe': 131.3, 'Cs': 132.9, 'Ba': 137.3,
        'La': 138.9, 'Ce': 140.1, 'Pr': 140.9, 'Nd': 144.2, 'Pm': 145.0, 'Sm': 150.4, 'Eu': 152.0, 'Gd': 157.3,
        'Tb': 158.9, 'Dy': 162.5, 'Ho': 164.9, 'Er': 167.3, 'Tm': 168.9, 'Yb': 173.0, 'Lu': 175.0, 'Hf': 178.5,
        'Ta': 180.9, 'W': 183.8, 'Re': 186.2, 'Os': 190.2, 'Ir': 192.2, 'Pt': 195.1, 'Au': 197.0, 'Hg': 200.6,
        'Tl': 204.4, 'Pb': 207.2, 'Bi': 208.9, 'Th': 232.0, 'Pa': 231.0, 'U': 238.0
      }
      def parse_formula(formula):
        import re
        pattern = r'([A-Z][a-z]?)(\d*)'
        matches = re.findall(pattern, formula)
        compound_dict = {}
        for (element, count) in matches:
            count = int(count) if count else 1
            if element in compound_dict:
                compound_dict[element] += count
            else:
                compound_dict[element] = count
        return compound_dict
      def calculate_molar_mass(compound_dict):
        molar_mass = 0.0
        for element, count in compound_dict.items():
            if element in atomic_masses:
                molar_mass += atomic_masses[element] * count
            else:
                raise ValueError(f"Element '{element}' is not in the atomic masses dictionary.")
        return molar_mass
      def main():
        formula = input("Enter the chemical formula of the compound: ")
        compound_dict = parse_formula(formula)
        molar_mass = calculate_molar_mass(compound_dict)
        print(f"The gram formula mass (molar mass) of {formula} is {molar_mass:.2f} g/mol")
      print("\nWhile using this function, please enter a valid input with correct capitilization.")
      while True:
        try:
          if __name__ == "__main__":
            main()
            break
        except:
          print("Invalid input. Please enter a valid chemical formula.")
def organic_rxns():
      def MlP(raw):
        #MLP - multilayer proccessor heh --< where q is lowered and stripped
        #Lambda COnfidience
        b = 0.14
        a = len(q)
        x = lambda a,b: a*b if a <= 36 else a*b + 5
        Confidience_Value = (100 - (x(a,b)))
        Confidience_Value = (f"With a reported confidience value of {Confidience_Value}%")
        #F1
        while " " not in raw or "-->" not in raw or "+" not in raw:
          print("Please align your equation to the specified syntax")
          raw = input("Whats is the chemical equation that corresponds to your organic reaction ").lower().strip()
        #F2
        while "c" not in raw or "h" not in raw:
          print("Your organic equation necessarily needs to have carbon and hydrogen atoms")
          raw = input("Whats is the chemical equation that corresponds to your organic reaction ").lower().strip()
        ester_key = ''
        p_1 = ''
        #Esterification, saponification bypass key, P_1 for addition/polymeri
        ab = raw.split(" --> ")
        if "+" in ab[0]:
          ester_key = "yes"
        elif "+" not in ab[0]:
          ester_key = "no"
        else:
          "frigidi"
        if "+" not in ab[1]:
          p_1 = "yes"
        elif "+" in ab[1]:
          p_1 = "no"
        else:
          ("frigidi")  
        #L1 --> remove special chars
        for i in raw:
          if i.isalnum() != True:
            raw = raw.replace(i, " ")
        #I1 for substitutions
        halides = ["f", "cl", "br", "i"]
        for i in halides:
          if i in raw:
            return print(f"The organic reaction,\n{q} is a substitution reaction\n{Confidience_Value}")
        x = []
        qdp = [] 
        qdr = []
        #L2 for seperation of the products and reatants
        while True:
          try:
            x = raw.split("     ")
            qdr = x[0]
            qdp = x[1]
            break
          except:
            print("Enter an equation which follows the specified syntax")
            raw = input("Enter your equation: ").strip()
            break
        pass #and y = yes/no to unlock split
        y = ""
        if ester_key == "yes":
          x = str(qdr).split("+")
          if " " in x[0]:
            y = x[0].split("   ")
          qdr_0 = y[0]
          qdr_1 = y[1]
          #I2 for saponification
          s_c = 0
          sap_marker_1 = ["na","k"]
          for i in sap_marker_1:
            if i in qdr:
              s_c += 1
          sapmarker_2 = "oh"
          if sapmarker_2 in qdr and qdp:
            s_c += 1
          if s_c == 2:
            return print(f"The organic reaction,\n{q} is an saponification reaction\n{Confidience_Value}")   
          #I3 for esterfiction
          estermarker = ["cooh", "oh", "ho"]
          for i in estermarker:
            if i in qdr_0 and qdr_1 and p_1 == "no":
              return print(f"The organic reaction,\n{q} is an esterfication reaction\n{Confidience_Value}")   
        #I4 for fermentation
        fermarker = ["alcohol", "lactic acid", "acetone", "propanol", "butanol", "pentanol", "oh"]
        for i in fermarker:
          if i in qdp:
            return print(f"The organic reaction,\n{q} is a fermentation reaction\n{Confidience_Value}")  
        #I5 for addition/polymerization
          #if theres a plus between reactants and one product 
        if ester_key == "yes" and p_1 == "yes":
          return print(f"The organic reaction,\n{q} is an addition OR polymerization reaction\n* Please verify with our resource to make a determination\n{Confidience_Value}") 
        #I6 for decomposition/cracking
        if ester_key == "no" and p_1 == "no":
           return print(f"The organic reaction,\n{q} is an decomposition OR cracking reaction\n*Please verify with our resource to make a determination\n{Confidience_Value}") 
        #I7 for combustion
        c = 0
        combmarker = ["o2", "co2", "h2o"]
        for i in combmarker:
          if i in qdp or qdr:
            c += 1
        if c >= 2:
          return print(f"The organic reaction,\n{q} is a combustion reaction\n{Confidience_Value}")
        print("Sorry, an untracable error has occured\nPlease consider contacting our support desk")
      print("Welcome to the organic reaction determiner\nPlease type more info for additional context!")
      q = input("Whats is the chemical equation that corresponds to your organic reaction: ").lower().strip()
      MlP(q)
def molcalc():
      def quantmol():
        q = float(input("How many moles?: \n\n"))
        w = input("What is the unit?: \n\n").strip()
        print("\n" + str((6.022*10**23)*q)+" "+w)
      def molquant():
        q = float(input("What is the quantity?: \n\n"))
        print("\n" + str(q/6.022*10**23)+" moles")
      def molvol():
        q = float(input("What is the volume in liters?: \n\n"))
        print("\n" + str(q/22.4)+" moles")
      def volmol():
        q = float(input("How many moles of the gas is there?: \n\n"))
        print("\n" + str(q*22.4)+" liters")
      while True:
        try:
          print("\n 1. Finding moles from volume(if a gas) \n 2. Finding volume from moles(if a gas) \n 3. Finding moles from quantity of substance \n 4. Finding quantity of substance from moles")
          x = input("Which one do you want to do?(Pick from 1-4):\n\n")
          if x == "1":
            molvol()
            break
          if x == "2":
            volmol()
            break
          if x == "3":
            molquant()
            break
          if x == "4":
            quantmol()
            break
        except:
          print("Try again")
    #prototypical %error
def percent_error():
      while True:
        mv = float(input("What is the measured value?\n"))
        av = float(input("What is the accepted value?\n"))
        pv = abs(float(mv)-float(av))/float(av)*100
        print("The percent error is ",str(pv)+"%\n")
        break
          #break
        #else:
          #print("Please enter a valid number.\n")
    #concentration
def concentrate():
      while True:
        dc = input("Type 1 for molarity, or 2 for ppm (parts per million).\n")
        if dc == "1": #molarity
          ms = input("How many moles of solute are present?\n")
          if ms.isdigit():
            vs = input("What is the volume of solution? (L)\n")
            if vs.isdigit():
              ml = float(ms)/float(vs)
              print(f"The molarity is",str(ml)+" M\n")
              break
        if dc == "2":#ppm
          p = input("What is the mass of your solute?\n")
          if p.isdigit():
            s = input("What is the mass of the whole solution? (solvent + solute)\n")
            if s.isdigit():
              ppm = float(p)/float(s)*1000000
              print("The concentration of your solution is ",str(ppm)+" PPM\n")
            else:
              print("idk what that number is, type it again.\n")
        break
    #heat
def heat():
      while True:
        f = input("What are you solving for? Type 'q' for heat, 'm' for mass or 'c' for specific heat capacity \n")
        if f == "q":
          m = float(input("What's the mass?\n"))
          c = float(input("What's the specific heat capacity?\n"))
          dt = float(input("What's the change in temperature? (⁰C)\n"))
          th = m*c*dt
          print("The heat is ",str(th)+" joules")
        if f == "m":
          q = float(input("What is the given heat? (J)\n"))
          c = float(input("What's the specific heat capacity?\n"))
          dt = float(input("What's the change in temperature? (⁰C)\n"))
          cdt = float(c)*float(dt)
          m = float(q)/float(cdt)
          print("The mass is ",str(m)+" grams\n")
        if f == "c":
          q = float(input("What is the given heat? (J)\n"))
          m = float(input("What's the mass? (g)\n"))
          dt = float(input("What's the change in temperature? (⁰C)\n"))
          mdt = float(dt)*float(m)
          c = float(q)/float(mdt)
          print("The SHC is ",str(c)+" grams\n")
        break
#main
skibidi=""
while True:
      try:
        print("\n 1. acid and base determiner \n", "2. combined gas law formula \n", "3. arhennius acid or base determiner \n", "4. significant figures \n", "5. organic groups \n", "6. finding if a compound is covalant or not \n", "7. finding alkanes,alkynes and alkenes \n", "8. percent composition \n", "9. grand formula mass(molar mass) \n", "10. organic reactions \n", "11. mole calculations \n", "12. percent error \n", "13. concentration (ppm or molarity) \n", "14. heat gain/loss (q = mc∆t)")
        skibidi = input("\nWhich type of question would you like to ask? Choose a number from 1-14(If you dont want to ask a question say none): \n \n")
        if skibidi == "1":
          acids_bases()
        elif skibidi == "2":
          combined_gas_formula()
        elif skibidi == "3":
          arhennius()
        elif skibidi == "4":
          sigfigs()
        elif skibidi == "5":
          organic_groups()
        elif skibidi == "6":
          polarity()
        elif skibidi == "7":
          alkynes_alkenes_alkanes()
        elif skibidi == "8":
          percent_comp()
        elif skibidi == "9":
          gfm()
        elif skibidi == "10":
          organic_rxns()
        elif skibidi == "11":
          molcalc()
        elif skibidi == "12":
          percent_error()
        elif skibidi == "13":
          concentrate()
        elif skibidi == "14":
          heat()
        elif skibidi == "none":
          print("\n scram")
          break
      except(ValueError, TypeError):
        print("\n Please enter a valid input \n")