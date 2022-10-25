
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BF545A"
    hexID = "SZKTRANSISTORFETBF545A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BF545A', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/BF545A_BF545B_BF545C.pdf', 'kicadSymbolki_keywords': 'N-Channel FET Transistor Low Voltage', 'kicadSymbolki_description': '5mA Idss, 30V Vgs, N-Channel JFET, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Transistor_FET : BF545A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

