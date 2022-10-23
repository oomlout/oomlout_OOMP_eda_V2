
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDC86244"
    hexID = "SZKTRANSISTORFETFDC86244"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FDC2512', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDC86244', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SuperSOT-6', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FDC86244-D.pdf', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '2.3A Id, 150V Vds, N-Channel MOSFET, 144mOhm Ron, SuperSOT-6', 'kicadSymbolki_fp_filters': 'SuperSOT*'}])
    newPart['name'].append('FDC86244')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

