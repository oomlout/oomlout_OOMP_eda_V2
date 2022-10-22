
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "C3D06065A"
    hexID = "SZKDIODEC3D665A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MBR735', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'C3D06065A', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-2_Vertical', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/65/C3D06065A.pdf', 'kicadSymbolki_keywords': 'sic diode', 'kicadSymbolki_description': '650V, 6A, SiC Schottky Diode, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('C3D06065A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

