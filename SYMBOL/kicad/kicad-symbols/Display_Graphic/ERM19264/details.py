
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Graphic"
    oIndex = "ERM19264"
    hexID = "SZKDIGRAPHICERM19264"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'DS', 'kicadSymbolValue': 'ERM19264', 'kicadSymbolFootprint': 'Display:ERM19264', 'kicadSymbolDatasheet': 'https://www.buydisplay.com/download/manual/ERM19264-1_Series_Datasheet.pdf', 'kicadSymbolki_keywords': 'display LCD graphic', 'kicadSymbolki_description': 'Graphics Display 192x64px,  8b parallel, 1/64 Duty, 3.3V or 5V VDD', 'kicadSymbolki_fp_filters': 'ERM19264*'}])
    newPart['name'].append('ERM19264')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

