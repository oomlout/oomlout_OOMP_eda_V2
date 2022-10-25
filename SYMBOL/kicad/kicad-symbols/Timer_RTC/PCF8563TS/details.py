
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_RTC"
    oIndex = "PCF8563TS"
    hexID = "SZKTIMERRTCPCF8563TS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCF8563TS', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/PCF8563.pdf', 'kicadSymbolki_keywords': 'I2C RTC Clock Calendar', 'kicadSymbolki_description': 'Realtime Clock/Calendar I2C Interface, TSSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Timer_RTC : PCF8563TS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

