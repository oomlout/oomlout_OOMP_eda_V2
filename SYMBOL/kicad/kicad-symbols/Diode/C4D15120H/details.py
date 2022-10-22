
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "C4D15120H"
    hexID = "SZKDIODEC4D1512H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C4D10120H', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'C4D15120H', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-247-2_Vertical', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/1190/C4D15120H.pdf', 'kicadSymbolki_keywords': 'sic diode', 'kicadSymbolki_description': '1200V, 15A, SiC Schottky Diode, TO-247', 'kicadSymbolki_fp_filters': 'TO?247*'}])
    newPart['name'].append('C4D15120H')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

