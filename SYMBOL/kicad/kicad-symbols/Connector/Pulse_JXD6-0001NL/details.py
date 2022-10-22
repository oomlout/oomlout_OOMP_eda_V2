
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Pulse_JXD6-0001NL"
    hexID = "SZKCNPULSEJXD61NL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Pulse_JXD6-0001NL', 'kicadSymbolFootprint': 'Connector_RJ:RJ45_Pulse_JXD6-0001NL_Horizontal', 'kicadSymbolDatasheet': 'https://productfinder.pulseeng.com/doc_type/WEB301/doc_num/JXD6-0001NL/doc_part/JXD6-0001NL.pdf', 'kicadSymbolki_keywords': 'lan jack transformer', 'kicadSymbolki_description': 'LAN Transformer Jack, RJ45, 10/100 BaseT', 'kicadSymbolki_fp_filters': 'RJ45*Pulse*JXD6?0001NL*'}])
    newPart['name'].append('Pulse_JXD6-0001NL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

