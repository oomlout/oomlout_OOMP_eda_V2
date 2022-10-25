
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog"
    oIndex = "AD630ARZ"
    hexID = "SZKANALOGAD63ARZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD630ARZ', 'kicadSymbolFootprint': 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ad630.pdf', 'kicadSymbolki_keywords': 'modulator demodulator', 'kicadSymbolki_description': 'High precision Balanced Modulator/Demodulator, 2 MHz, SOIC-20W', 'kicadSymbolki_fp_filters': 'SOIC*7.5x12.8mm*P1.27mm*'}])
    newPart['name'].append('Analog : AD630ARZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

