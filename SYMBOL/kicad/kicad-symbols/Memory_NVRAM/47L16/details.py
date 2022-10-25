
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_NVRAM"
    oIndex = "47L16"
    hexID = "SZKMEMORYNVRAM47L16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '47L04', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '47L16', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20005371C.pdf', 'kicadSymbolki_keywords': '16kb 3V I2C serial EERAM SRAM EEPROM', 'kicadSymbolki_description': '16kbit I2C serial EERAM, SRAM with EEPROM backup, 2.7-3.6V, DIP-8/SOIC-8/TSSOP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm* TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('Memory_NVRAM : 47L16')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

