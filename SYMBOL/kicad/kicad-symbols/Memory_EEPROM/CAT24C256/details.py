
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "CAT24C256"
    hexID = "SZKMEMORYEEPROMCAT24C256"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '24LC16', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CAT24C256', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.onsemi.cn/PowerSolutions/document/CAT24C256-D.PDF', 'kicadSymbolki_keywords': 'I2C EEPROM Serial 256kb', 'kicadSymbolki_description': '256 kb CMOS Serial EEPROM, DIP-8/SOIC-8/TSSOP-8/DFN-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm* TSSOP*4.4x3mm*P0.65mm* DFN*3x2mm*P0.5mm*'}])
    newPart['name'].append('CAT24C256')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

