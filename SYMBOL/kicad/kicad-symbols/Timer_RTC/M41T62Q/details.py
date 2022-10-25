
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_RTC"
    oIndex = "M41T62Q"
    hexID = "SZKTIMERRTCM41T62Q"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'M41T62Q', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_3x3mm_P0.5mm_EP1.8x1.8mm', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/m41t62.pdf', 'kicadSymbolki_keywords': 'I2C RTC Alarm interrupt', 'kicadSymbolki_description': 'Low-power I2C RTC with alarm interrupt QFN', 'kicadSymbolki_fp_filters': 'QFN*16*1EP*3x3mm*P0.5mm*EP1.8x1.8mm*'}])
    newPart['name'].append('Timer_RTC : M41T62Q')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

