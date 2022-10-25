
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Timer_RTC"
    oIndex = "MCP7940N-xST"
    hexID = "SZKTIMERRTCMCP794NXST"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MCP7940N-xMS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP7940N-xST', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005010F.pdf', 'kicadSymbolki_keywords': 'realtime clock RTC', 'kicadSymbolki_description': 'Real-Time Clock, I2C, Battery Backup, TSSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* TSSOP*4.4x3mm*P0.65mm* MSOP*3x3mm*P0.65mm* DIP*W7.62mm*'}])
    newPart['name'].append('Timer_RTC : MCP7940N-xST')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

