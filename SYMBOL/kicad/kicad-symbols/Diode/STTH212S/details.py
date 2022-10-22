
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "STTH212S"
    hexID = "SZKDIODESTTH212S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'STTH212S', 'kicadSymbolFootprint': 'Diode_SMD:D_SMC', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/stth212.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '1200V 2A High Voltage Ultrafast Diode, SMC', 'kicadSymbolki_fp_filters': 'D?SMC*'}])
    newPart['name'].append('STTH212S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

