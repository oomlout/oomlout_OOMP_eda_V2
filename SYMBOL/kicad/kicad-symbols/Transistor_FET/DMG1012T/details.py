
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "DMG1012T"
    hexID = "SZKTRANSISTORFETDMG112T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'DMG1012T', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-523', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/ds31783.pdf', 'kicadSymbolki_keywords': 'N-Channel MOSFET', 'kicadSymbolki_description': '20V Vds, 0.63 Id, N-Channel MOSFET with ESD protection, SOT-523', 'kicadSymbolki_fp_filters': 'SOT?523*'}])
    newPart['name'].append('DMG1012T')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

