
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog"
    oIndex = "AD637xQ"
    hexID = "SZKANALOGAD637XQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD637xQ', 'kicadSymbolFootprint': 'Package_DIP:DIP-14_W7.62mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD637.pdf', 'kicadSymbolki_keywords': 'rms-to-dc', 'kicadSymbolki_description': 'High Precision, Wideband RMS-to-DC Converter, DIP-14', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Analog : AD637xQ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

