
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "C3D03060E"
    hexID = "SZKDIODEC3D36E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CSD01060E', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'C3D03060E', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2_TabPin1', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/119/C3D03060E.pdf', 'kicadSymbolki_keywords': 'sic diode', 'kicadSymbolki_description': '600V, 3A, SiC Schottky Diode, TO-252', 'kicadSymbolki_fp_filters': 'TO?252*TabPin1*'}])
    newPart['name'].append('Diode : C3D03060E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

