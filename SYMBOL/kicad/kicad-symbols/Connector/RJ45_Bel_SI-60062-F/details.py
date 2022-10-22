
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "RJ45_Bel_SI-60062-F"
    hexID = "SZKCNRJ45BELSI662F"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'RJ45_Bel_SI-60062-F', 'kicadSymbolFootprint': 'Connector_RJ:RJ45_Bel_SI-60062-F', 'kicadSymbolDatasheet': 'https://belfuse.com/resources/drawings/magneticsolutions/dr-mag-si-60062-f.pdf', 'kicadSymbolki_keywords': 'RJ45 Magjack', 'kicadSymbolki_description': '1 Port RJ45 Magjack Connector Through Hole 10/100 Base-T, AutoMDIX', 'kicadSymbolki_fp_filters': 'RJ45*Bel*SI*60062*F*'}])
    newPart['name'].append('RJ45_Bel_SI-60062-F')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

