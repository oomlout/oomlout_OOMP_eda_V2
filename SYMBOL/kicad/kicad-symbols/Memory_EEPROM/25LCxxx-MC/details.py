
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "25LCxxx-MC"
    hexID = "SZKMEMORYEEPROM25LCXXXMC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': '25LCxxx-MC', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x2mm_P0.5mm_EP1.75x1.45mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21832H.pdf', 'kicadSymbolki_keywords': 'EEPROM memory SPI serial', 'kicadSymbolki_description': 'SPI Serial EEPROM, DFN8', 'kicadSymbolki_fp_filters': 'DFN*3x2mm*P0.5mm*'}])
    newPart['name'].append('Memory_EEPROM : 25LCxxx-MC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

