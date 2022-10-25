
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BSC030N08NS5"
    hexID = "SZKTRANSISTORFETBSC3N8NS5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CSD17578Q5A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSC030N08NS5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TDSON-8-1', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-BSC030N08NS5-DS-v02_02-EN.pdf?fileId=5546d4624ad04ef9014aed52f4210acf', 'kicadSymbolki_keywords': 'OptiMOS Power MOSFET N-MOS', 'kicadSymbolki_description': '100A Id, 80V Vds, OptiMOS N-Channel Power MOSFET, 3.0mOhm Ron, Qg (typ) 61.0nC, PG-TDSON-8', 'kicadSymbolki_fp_filters': 'TDSON*'}])
    newPart['name'].append('Transistor_FET : BSC030N08NS5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

