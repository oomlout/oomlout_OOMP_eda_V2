
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "CAT24C128"
    hexID = "SZKMEMORYEEPROMCAT24C128"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '24LC16', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CAT24C128', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/CAT24C128-D.PDF', 'kicadSymbolki_keywords': 'I2C EEPROM Serial 128kb', 'kicadSymbolki_description': '128 kb CMOS Serial EEPROM, SOIC-8/TSSOP-8/DFN-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm* TSSOP*4.4x3mm*P0.65mm* DFN*3x2mm*P0.5mm*'}])
    newPart['name'].append('Memory_EEPROM : CAT24C128')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

