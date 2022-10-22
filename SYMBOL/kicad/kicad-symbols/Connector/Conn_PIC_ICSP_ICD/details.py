
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Connector"
    oIndex = "Conn_PIC_ICSP_ICD"
    hexID = "SZKCNCONNPICICSPICD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'Conn_PIC_ICSP_ICD', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/30277d.pdf', 'kicadSymbolki_keywords': 'icsp icd pic microchip', 'kicadSymbolki_description': 'Microchip PIC In-Circuit Serial Programming/Debugging (ICSP/ICD) connector', 'kicadSymbolki_fp_filters': 'PinHeader*1x06*P2.54mm* PinSocket*1x06*P2.54mm*'}])
    newPart['name'].append('Conn_PIC_ICSP_ICD')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

