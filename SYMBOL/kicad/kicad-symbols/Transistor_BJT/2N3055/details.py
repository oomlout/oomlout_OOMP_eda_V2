
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "2N3055"
    hexID = "SZKTRANSISTORBJT2N355"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': '2N3055', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-3', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/2N3055-D.PDF', 'kicadSymbolki_keywords': 'power NPN Transistor', 'kicadSymbolki_description': '15A Ic, 60V Vce, Power NPN Transistor, TO-3', 'kicadSymbolki_fp_filters': 'TO?3*'}])
    newPart['name'].append('2N3055')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

