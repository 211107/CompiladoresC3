import re

class Converso():
    
    def __init__(self, code: str):
        self.code = code
        
    def initConverso(self):
        code = ""
        
        lineas = self.code.splitlines()
        esLLamadaFun = True
                
        for line in lineas:            
                                    
            if("var" in line):                
                code = code + re.sub(r'var\s+(\w+)', r'\1 =', line).replace("int", "0") + "\n"                
                
            if("imprimir" in line):                
                code = code + re.sub(r'\bimprimir\w*\b', lambda match: match.group().replace("imprimir", "print"), line) + "\n" 
                esLLamadaFun = False
                
            if("leer" in line):
                variable = ""
                leer = False                
                for i in range(len(line)):
                                            
                    if(line[i] == "("):
                        leer = True        
                                                                                                            
                    if( (line[i] == ")") ):                                
                        leer = False        
                                        
                    if(leer):                        
                        variable =  variable + line[i]
                    
                code = code + (line.find('l')*" ") + variable[1:] + ' = input()' + "\n"  
                esLLamadaFun = False
                
            if("fun" in line):
                code = code + re.sub(r'fun\s+(\w+)\(\)\s*{', r'def \1():', line) + "\n"     
                
            if("mientras" in line):
                code = code + re.sub(r'mientras\s+verdadero\s+{', r'while True:', line) + "\n"    
            
            patron = r"^\w+\(\)$"
            if( re.match(patron, line) and esLLamadaFun):
                code = code + line + "\n"                            
                
            if("romper" in line):
                code = code + line.replace("romper","break") + "\n"     
                
            if("si" in line):                     
                block = ""   
                temp = line                                
                line = line.strip()                
                line = re.sub(r'\s+', ' ', line)
                array=line.split(" ")
                if(array[0] == "si"):                                        
                    block = temp.find('s')*" "
                    code = code + block + line.replace("si","if").replace("{",":") + "\n"
                else:
                    block = temp.find('}')*" "        
                    code = code + block + line.replace("sino","else").replace("}","").replace("{",":")[1:] + "\n"
            
            _patron = re.compile(r'\w+\s*=\s*.+')            
            if(_patron.findall(line)):
                code = code + line + "\n"
            
            esLLamadaFun = True
        print("convetido")
        print(code)
                                            
        return code
    
