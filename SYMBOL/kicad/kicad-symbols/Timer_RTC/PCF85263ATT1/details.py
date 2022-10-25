
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_RTC"
    oIndex = "PCF85263ATT1"
    hexID = "SZKTIMERRTCPCF85263ATT1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCF85263ATT1', 'kicadSymbolFootprint': 'Package_SO:TSSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/PCF85263A.pdf', 'kicadSymbolki_keywords': 'RTC battery I2C', 'kicadSymbolki_description': 'Tiny Real-Time Clock/calendar with alarm function, battery switch-over, time stamp input, I2C bus, TSSOP-10', 'kicadSymbolki_fp_filters': 'TSSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Timer_RTC : PCF85263ATT1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

