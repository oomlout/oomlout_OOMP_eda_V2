
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "C3D04060A"
    hexID = "SZKDIODEC3D46A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MBR735', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'C3D04060A', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-2_Vertical', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/845/C3D04060A.pdf', 'kicadSymbolki_keywords': 'sic diode', 'kicadSymbolki_description': '600V, 4A, SiC Schottky Diode, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Diode : C3D04060A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

