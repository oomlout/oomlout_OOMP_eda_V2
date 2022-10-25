
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "AK5394AVS"
    hexID = "SZKAUDIOAK5394AVS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AK5394AVS', 'kicadSymbolFootprint': 'Package_SO:SOIC-28W_7.5x18.7mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.akm.com/akm/en/file/datasheet/AK5394AVS.pdf', 'kicadSymbolki_keywords': 'audio adc 2ch 24bit 192kHz', 'kicadSymbolki_description': 'Super High Performance 192kHz 24-Bit Sigma-Delta ADC, SOIC-28', 'kicadSymbolki_fp_filters': 'SOIC*7.5x18.7mm*P1.27mm*'}])
    newPart['name'].append('Audio : AK5394AVS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

