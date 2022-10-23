
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "FDG1024NZ"
    hexID = "SZKTRANSISTORFETFDG124NZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'FDG1024NZ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FDG1024NZ-D.pdf', 'kicadSymbolki_keywords': 'Dual N-Channel MOSFET Logic Level', 'kicadSymbolki_description': '1.2A Id, 20V Vds, Dual N-Channel MOSFET, 175mOhm Ron, SC-70-6', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('FDG1024NZ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

