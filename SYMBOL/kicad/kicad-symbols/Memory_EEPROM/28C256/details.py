
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "28C256"
    hexID = "SZKMEMORYEEPROM28C256"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '28C256', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/doc0006.pdf', 'kicadSymbolki_keywords': 'Parallel EEPROM 256Kb', 'kicadSymbolki_description': 'Paged Parallel EEPROM 256Kb (32K x 8), DIP-28/SOIC-28', 'kicadSymbolki_fp_filters': 'DIP*W15.24mm* SOIC*7.5x17.9mm*P1.27mm*'}])
    newPart['name'].append('Memory_EEPROM : 28C256')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

