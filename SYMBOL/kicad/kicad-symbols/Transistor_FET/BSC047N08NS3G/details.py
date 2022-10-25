
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BSC047N08NS3G"
    hexID = "SZKTRANSISTORFETBSC47N8NS3G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CSD17578Q5A', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSC047N08NS3G', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TDSON-8-1', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-BSC047N08NS3G-DS-v02_07-en.pdf?fileId=db3a30431add1d95011ae7e8dacf5611', 'kicadSymbolki_keywords': 'OptiMOS Power MOSFET N-MOS', 'kicadSymbolki_description': '100A Id, 80V Vds, OptiMOS N-Channel Power MOSFET, 4.7mOhm Ron, Qg (typ) 52.0nC, PG-TDSON-8', 'kicadSymbolki_fp_filters': 'TDSON*'}])
    newPart['name'].append('Transistor_FET : BSC047N08NS3G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

