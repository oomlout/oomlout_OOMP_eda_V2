
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "DWM1001"
    hexID = "SZKRFMODWM11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DWM1001', 'kicadSymbolFootprint': 'RF_Module:DecaWave_DWM1001', 'kicadSymbolDatasheet': 'https://www.decawave.com/sites/default/files/dwm1001_datasheet.pdf', 'kicadSymbolki_keywords': 'DWM1000  DecaWave RF ranging UWB', 'kicadSymbolki_description': ' Ultra wide band RF module With ranging location capabilities, I2C, UART, SPI, +2.8V to +3.6V VCC', 'kicadSymbolki_fp_filters': '*DWM1001*'}])
    newPart['name'].append('RF_Module : DWM1001')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

