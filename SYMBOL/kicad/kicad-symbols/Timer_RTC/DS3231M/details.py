
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_RTC"
    oIndex = "DS3231M"
    hexID = "SZKTIMERRTCDS3231M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS3231M', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/DS3231.pdf', 'kicadSymbolki_keywords': 'RTC TCXO Realtime Time Clock Crystal Oscillator I2C', 'kicadSymbolki_description': 'Extremely Accurate I2C-Integrated RTC/TCXO/Crystal SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('Timer_RTC : DS3231M')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

