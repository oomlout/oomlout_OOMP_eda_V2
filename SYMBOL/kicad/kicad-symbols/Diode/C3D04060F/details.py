
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "C3D04060F"
    hexID = "SZKDIODEC3D46F"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C3D02060F', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'C3D04060F', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220F-2_Vertical', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/41/C3D04060F.pdf', 'kicadSymbolki_keywords': 'sic diode', 'kicadSymbolki_description': '600V, 4A, SiC Schottky Diode, TO-220F', 'kicadSymbolki_fp_filters': 'TO?220F*'}])
    newPart['name'].append('C3D04060F')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

