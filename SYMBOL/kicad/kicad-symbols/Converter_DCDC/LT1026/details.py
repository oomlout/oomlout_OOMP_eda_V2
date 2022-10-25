
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "LT1026"
    hexID = "SZKCONLT126"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1026', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/1026fb.pdf', 'kicadSymbolki_keywords': 'monolithic switched capacitor voltage doubler inverter ', 'kicadSymbolki_description': 'voltage doubler and inverter', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Converter_DCDC : LT1026')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

