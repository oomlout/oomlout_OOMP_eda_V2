
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_RTC"
    oIndex = "DS1602"
    hexID = "SZKTIMERRTCDS162"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS1602', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/DS1602.pdf', 'kicadSymbolki_keywords': 'Elapsed Time Counter', 'kicadSymbolki_description': 'Elapsed Time Counter, -40 to +85 C, 2.5V to 5.5V VCC, DIP-8, SO-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SO*5.3x6.2mm?P1.27mm*'}])
    newPart['name'].append('DS1602')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

