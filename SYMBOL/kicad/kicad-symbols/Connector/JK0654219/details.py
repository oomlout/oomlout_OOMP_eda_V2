
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "JK0654219"
    hexID = "SZKCNJK654219"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'JK0654219', 'kicadSymbolFootprint': 'Connector_RJ:RJ45_Pulse_JK0654219NL_Horizontal', 'kicadSymbolDatasheet': 'https://media.digikey.com/pdf/Data%20Sheets/Pulse%20PDFs/JK%20Series.pdf', 'kicadSymbolki_keywords': '8P8C RJ female connector', 'kicadSymbolki_description': ' 1 Port RJ45 Magjack Connector Through Hole 10/100/1000 Base-T, AutoMDIX', 'kicadSymbolki_fp_filters': 'RJ45*Pulse*JK0654219NL*'}])
    newPart['name'].append('JK0654219')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

