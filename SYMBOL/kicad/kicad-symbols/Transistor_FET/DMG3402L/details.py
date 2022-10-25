
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "DMG3402L"
    hexID = "SZKTRANSISTORFETDMG342L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSS138', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'DMG3402L', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'http://www.diodes.com/assets/Datasheets/DMG3402L.pdf', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '4A Id, 30V Vds, N-Channel MOSFET, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Transistor_FET : DMG3402L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

