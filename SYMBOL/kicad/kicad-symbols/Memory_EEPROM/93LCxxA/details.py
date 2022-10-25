
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "93LCxxA"
    hexID = "SZKMEMORYEEPROM93LCXXA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '93LCxxA', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/20001749K.pdf', 'kicadSymbolki_keywords': 'EEPROM memory Microwire', 'kicadSymbolki_description': 'Serial EEPROM, 93 Series, 2.5V, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*'}])
    newPart['name'].append('Memory_EEPROM : 93LCxxA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

