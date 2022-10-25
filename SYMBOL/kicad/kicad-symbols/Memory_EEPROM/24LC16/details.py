
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "24LC16"
    hexID = "SZKMEMORYEEPROM24LC16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '24LC16', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21703d.pdf', 'kicadSymbolki_keywords': 'I2C Serial EEPROM', 'kicadSymbolki_description': 'I2C Serial EEPROM, 16Kb, DIP-8/SOIC-8/TSSOP-8/DFN-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm* TSSOP*4.4x3mm*P0.65mm* DFN*3x2mm*P0.5mm*'}])
    newPart['name'].append('Memory_EEPROM : 24LC16')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

