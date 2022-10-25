
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_RTC"
    oIndex = "PCF85263AT"
    hexID = "SZKTIMERRTCPCF85263AT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCF85263AT', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/PCF85263A.pdf', 'kicadSymbolki_keywords': 'RTC battery I2C', 'kicadSymbolki_description': 'Tiny Real-Time Clock/calendar with alarm function, battery switch-over, time stamp input, I2C bus, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Timer_RTC : PCF85263AT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

