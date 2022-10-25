
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "C4D10120A"
    hexID = "SZKDIODEC4D112A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MBR735', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'C4D10120A', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-2_Vertical', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/82/C4D10120A.pdf', 'kicadSymbolki_keywords': 'sic diode', 'kicadSymbolki_description': '1200V, 10A, SiC Schottky Diode, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Diode : C4D10120A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

