
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "C3D08060G"
    hexID = "SZKDIODEC3D86G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C3D06060G', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'C3D08060G', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-2_TabPin1', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/141/C3D08060G.pdf', 'kicadSymbolki_keywords': 'sic diode', 'kicadSymbolki_description': '600V, 8A, SiC Schottky Diode, TO-263', 'kicadSymbolki_fp_filters': 'TO?263*TabPin1*'}])
    newPart['name'].append('C3D08060G')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

