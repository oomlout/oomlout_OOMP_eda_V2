
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BSC109N10NS3G"
    hexID = "SZKTRANSISTORFETBSC19N1NS3G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CSD17578Q5A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSC109N10NS3G', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TDSON-8-1', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-BSC109N10NS3-DS-v02_00-en.pdf?fileId=db3a304327b897500128247bdae36f3f', 'kicadSymbolki_keywords': 'OptiMOS Power MOSFET N-MOS', 'kicadSymbolki_description': '63A Id, 100V Vds, OptiMOS N-Channel Power MOSFET, 10.9mOhm Ron, Qg (typ) 26.0nC, PG-TDSON-8', 'kicadSymbolki_fp_filters': 'TDSON*'}])
    newPart['name'].append('Transistor_FET : BSC109N10NS3G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

