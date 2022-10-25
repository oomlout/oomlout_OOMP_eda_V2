
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "TMS4C1050N"
    hexID = "SZKMEMORYEEPROMTMS4C15N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMS4C1050N', 'kicadSymbolFootprint': 'Package_DIP:DIP-16_W7.62mm', 'kicadSymbolDatasheet': 'http://www.datasheets360.com/pdf/3640170882560205603', 'kicadSymbolki_keywords': 'Field Memory', 'kicadSymbolki_description': 'Field Memory, 262264 x 4 bit, [Obsolete 1992-01]', 'kicadSymbolki_fp_filters': 'DIP*'}])
    newPart['name'].append('Memory_EEPROM : TMS4C1050N')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

