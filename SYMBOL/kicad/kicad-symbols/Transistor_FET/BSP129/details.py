
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BSP129"
    hexID = "SZKTRANSISTORFETBSP129"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSP129', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-BSP129-DS-v01_42-en.pdf?fileId=db3a30433c1a8752013c1fc296d2395f', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '0.35A Id, 240V Vds, N-Channel MOSFET, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('Transistor_FET : BSP129')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

