
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_RTC"
    oIndex = "PCF85063ATL"
    hexID = "SZKTIMERRTCPCF8563ATL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCF85063ATL', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-10-1EP_2.6x2.6mm_P0.5mm_EP1.3x2.2mm', 'kicadSymbolDatasheet': 'https://www.nxp.com/docs/en/data-sheet/PCF85063A.pdf', 'kicadSymbolki_keywords': 'RTC I2C', 'kicadSymbolki_description': 'I2C Real-Time Clock Calendar w/ Alarm, DFN-10', 'kicadSymbolki_fp_filters': 'DFN*2.6x2.6mm*P0.5mm*'}])
    newPart['name'].append('Timer_RTC : PCF85063ATL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

