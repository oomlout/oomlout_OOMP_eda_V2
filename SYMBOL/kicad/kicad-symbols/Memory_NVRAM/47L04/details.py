
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_NVRAM"
    oIndex = "47L04"
    hexID = "SZKMEMORYNVRAM47L4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '47L04', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005371C.pdf', 'kicadSymbolki_keywords': '4kb 3V I2C serial EERAM SRAM EEPROM', 'kicadSymbolki_description': '4kbit I2C serial EERAM, SRAM with EEPROM backup, 2.7-3.6V, DIP-8/SOIC-8/TSSOP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm* TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Memory_NVRAM : 47L04')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

