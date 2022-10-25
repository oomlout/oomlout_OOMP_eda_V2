
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "C3D30065D"
    hexID = "SZKDIODEC3D365D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C3D16060D', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'C3D30065D', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-247-3_Vertical', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/969/C3D30065D.pdf', 'kicadSymbolki_keywords': 'sic diode', 'kicadSymbolki_description': '650V, 30A, SiC Schottky Diode, TO-247-3', 'kicadSymbolki_fp_filters': 'TO?247*'}])
    newPart['name'].append('Diode : C3D30065D')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

