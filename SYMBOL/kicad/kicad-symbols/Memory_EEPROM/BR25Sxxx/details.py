
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Memory_EEPROM"
    oIndex = "BR25Sxxx"
    hexID = "SZKMEMORYEEPROMBR25SXXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '25LCxxx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BR25Sxxx', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.rohm.com/web/global/products/-/product/BR25G128F-3', 'kicadSymbolki_keywords': 'EEPROM memory SPI serial', 'kicadSymbolki_description': 'ROHM Semiconductor SPI Serial EEPROM, DIP-8/SOIC-8/TSSOP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm* TSSOP*4.4x3mm*P0.65mm*'}])
    newPart['name'].append('BR25Sxxx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

