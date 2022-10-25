
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "DMN30H4D0L"
    hexID = "SZKTRANSISTORFETDMN3H4DL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BSS138', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'DMN30H4D0L', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'http://www.diodes.com/assets/Datasheets/DMN30H4D0L.pdf', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '0.25A Id, 300V Vds, N-Channel MOSFET, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Transistor_FET : DMN30H4D0L')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

