
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "BSS138"
    hexID = "SZKTRANSISTORFETBSS138"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BSS138', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/BSS138-D.PDF', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '50V Vds, 0.22A Id, N-Channel MOSFET, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Transistor_FET : BSS138')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

