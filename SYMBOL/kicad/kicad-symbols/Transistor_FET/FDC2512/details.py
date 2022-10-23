
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDC2512"
    hexID = "SZKTRANSISTORFETFDC2512"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDC2512', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SuperSOT-6', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FDC2512-D.pdf', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '1.4A Id, 150V Vds, N-Channel MOSFET, 425mOhm Ron, SuperSOT-6', 'kicadSymbolki_fp_filters': 'SuperSOT*'}])
    newPart['name'].append('FDC2512')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

