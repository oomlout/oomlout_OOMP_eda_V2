
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_RTC"
    oIndex = "DS1302S+"
    hexID = "SZKTIMERRTCDS132S+"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS1302S+', 'kicadSymbolFootprint': 'Package_SO:SO-8_5.3x6.2mm_P1.27mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/DS1302.pdf', 'kicadSymbolki_keywords': 'RTC, Trickle-Charge Timekeeping Chip', 'kicadSymbolki_description': 'Trickle-Charge Timekeeping Chip, 2.0V to 5.5V VCC, 0°C to +70°C, SO-8', 'kicadSymbolki_fp_filters': 'SO*5.3x6.2mm?P1.27mm*'}])
    newPart['name'].append('Timer_RTC : DS1302S+')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

