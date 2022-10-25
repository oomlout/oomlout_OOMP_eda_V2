
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "C3D10170H"
    hexID = "SZKDIODEC3D117H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C4D10120H', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'C3D10170H', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-247-2_Vertical', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/96/C3D10170H.pdf', 'kicadSymbolki_keywords': 'sic diode', 'kicadSymbolki_description': '1700V, 10A, SiC Schottky Diode, TO-247', 'kicadSymbolki_fp_filters': 'TO?247*'}])
    newPart['name'].append('Diode : C3D10170H')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

