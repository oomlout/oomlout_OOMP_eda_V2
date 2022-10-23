
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_MMI_Q5-100"
    hexID = "SZKSWITCHSWIQ51"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SW_E3_SA3216', 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_MMI_Q5-100', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://latest.ledswitches.co.uk/media/pdf/Q5-PCB-V1-withQ5data.pdf', 'kicadSymbolki_keywords': 'switch normally-open pushbutton push-button LCD', 'kicadSymbolki_description': 'Push button switch with LCD screen', 'kicadSymbolki_fp_filters': 'SW?PUSH?LCD?E3?SAxxxx*'}])
    newPart['name'].append('SW_MMI_Q5-100')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

