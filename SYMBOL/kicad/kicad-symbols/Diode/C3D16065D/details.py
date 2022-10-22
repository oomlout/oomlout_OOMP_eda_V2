
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "C3D16065D"
    hexID = "SZKDIODEC3D1665D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C3D16060D', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'C3D16065D', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-247-3_Vertical', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/99/C3D16065D.pdf', 'kicadSymbolki_keywords': 'sic diode', 'kicadSymbolki_description': '650V, 16A, SiC Schottky Diode, TO-247-3', 'kicadSymbolki_fp_filters': 'TO?247*'}])
    newPart['name'].append('C3D16065D')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

