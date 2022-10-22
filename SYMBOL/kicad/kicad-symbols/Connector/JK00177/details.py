
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "JK00177"
    hexID = "SZKCNJK177"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'JK00177', 'kicadSymbolFootprint': 'Connector_RJ:RJ45_Pulse_JK00177NL_Horizontal', 'kicadSymbolDatasheet': 'https://productfinder.pulseeng.com/doc_type/WEB301/doc_num/J432/doc_part/J432.pdf', 'kicadSymbolki_keywords': '8P8C RJ female connector POE', 'kicadSymbolki_description': ' 1 Port RJ45 Magjack Connector Through Hole 10/100/1000 Base-T, AutoMDIX, 75W POE', 'kicadSymbolki_fp_filters': 'RJ45*Pulse*JK00177NL*'}])
    newPart['name'].append('JK00177')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

