
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BSC070N10NS5"
    hexID = "SZKTRANSISTORFETBSC7N1NS5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CSD17578Q5A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSC070N10NS5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TDSON-8-1', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-BSC070N10NS5-DS-v02_01-EN.pdf?fileId=5546d4624a0bf290014a0fc62d9d6b3c', 'kicadSymbolki_keywords': 'OptiMOS Power MOSFET N-MOS', 'kicadSymbolki_description': '80A Id, 100V Vds, OptiMOS N-Channel Power MOSFET, 7.0mOhm Ron, Qg (typ) 30.0nC, PG-TDSON-8', 'kicadSymbolki_fp_filters': 'TDSON*'}])
    newPart['name'].append('Transistor_FET : BSC070N10NS5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

