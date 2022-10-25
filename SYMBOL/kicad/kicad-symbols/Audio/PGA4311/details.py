
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Audio"
    oIndex = "PGA4311"
    hexID = "SZKAUDIOPGA4311"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PGA4311', 'kicadSymbolFootprint': 'Package_SO:SOIC-28W_7.5x17.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/pga4311.pdf', 'kicadSymbolki_keywords': 'audio volume control 4ch spi', 'kicadSymbolki_description': '4-Channel Audio Volume Control, SPI Interface, +31.5dB to -95.5dB, SOIC-28W', 'kicadSymbolki_fp_filters': 'SOIC*7.5x17.9mm*P1.27mm*'}])
    newPart['name'].append('Audio : PGA4311')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

