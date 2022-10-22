
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "AK5393VS"
    hexID = "SZKAUDIOAK5393VS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AK5393VS', 'kicadSymbolFootprint': 'Package_SO:SOIC-28W_7.5x18.7mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.akm.com/akm/en/file/datasheet/AK5393VS.pdf', 'kicadSymbolki_keywords': 'audio adc 2ch 24bit 96kHz', 'kicadSymbolki_description': 'Enhanced Dual Bit Sigma-Delta 96kHz 24-Bit ADC, SOIC-28', 'kicadSymbolki_fp_filters': 'SOIC*7.5x18.7mm*P1.27mm*'}])
    newPart['name'].append('AK5393VS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

