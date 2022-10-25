
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_RTC"
    oIndex = "PCF8523TK"
    hexID = "SZKTIMERRTCPCF8523TK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCF8523TK', 'kicadSymbolFootprint': 'Package_SON:HVSON-8-1EP_4x4mm_P0.8mm_EP2.2x3.1mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/PCF8523.pdf', 'kicadSymbolki_keywords': 'I2C RTC Clock Calendar', 'kicadSymbolki_description': 'Realtime Clock/Calendar I2C Interface, HVSON-8', 'kicadSymbolki_fp_filters': 'HVSON*1EP*4x4mm*P0.8mm*'}])
    newPart['name'].append('Timer_RTC : PCF8523TK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

