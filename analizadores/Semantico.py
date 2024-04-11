import re


class Semantic():
    
    def __init__(self, code : str):
        self.code = code
    
    def apply(self):
        
        lineas = self.code.splitlines()
        
        pilaVariables = []        
        pilaFunciones = []        
        
        for line in lineas:

            if("var" in line):                               
                temp = re.sub(r'\s+', ' ', line.strip())                
                pilaVariables.append(temp.split(" ")[1])
                
            if("fun" in line):                                
                temp = re.sub(r'\s+', ' ', line.strip())                
                pilaFunciones.append(temp.split(" ")[1])
        
        blockVariablesRepetidas = ""
        blockFucnionesRepetidas = ""
        BRTS = False        
        dupV = [x for i, x in enumerate(pilaVariables) if i != pilaVariables.index(x)]        
        if(not(len(dupV) == 0)):
            blockVariablesRepetidas = "Esta variable ya esta declarada: " + str(dupV)
            BRTS = True        
        dupF = [x for i, x in enumerate(pilaFunciones) if i != pilaFunciones.index(x)]
        if(not(len(dupF) == 0)):
            blockFucnionesRepetidas = "Esta función ya esta declarada: " + str(dupF)
            BRTS = True               
        if(BRTS):
            return blockVariablesRepetidas, blockFucnionesRepetidas 
        else:
            return None
            
        
        