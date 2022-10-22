
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "C4D10120E"
    hexID = "SZKDIODEC4D112E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CSD01060E', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'C4D10120E', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2_TabPin1', 'kicadSymbolDatasheet': 'https://www.wolfspeed.com/media/downloads/134/C4D10120E.pdf', 'kicadSymbolki_keywords': 'sic diode', 'kicadSymbolki_description': '1200V, 10A, SiC Schottky Diode, TO-252', 'kicadSymbolki_fp_filters': 'TO?252*TabPin1*'}])
    newPart['name'].append('C4D10120E')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

