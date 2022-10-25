
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "ADuM3152"
    hexID = "SZKISOLATORADUM3152"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADuM3152', 'kicadSymbolFootprint': 'Package_SO:SSOP-20_5.3x7.2mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADuM3151_3152_3153.pdf', 'kicadSymbolki_keywords': 'spi isolated', 'kicadSymbolki_description': '3.75kV 7-Channel SPI Isolator, 2 Reverse Channels, SSOP-20', 'kicadSymbolki_fp_filters': 'SSOP*5.3x7.2mm*P0.65mm*'}])
    newPart['name'].append('Isolator : ADuM3152')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

