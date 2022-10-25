
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor"
    oIndex = "ADE7763xRS"
    hexID = "SZKSENADE7763XRS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADE7763xRS', 'kicadSymbolFootprint': 'Package_SO:SSOP-20_5.3x7.2mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADE7763.pdf', 'kicadSymbolki_keywords': 'Energy Metering', 'kicadSymbolki_description': 'Single-Phase Active and Apparent Energy Metering, SSOP-20', 'kicadSymbolki_fp_filters': 'SSOP*5.3x7.2mm*P0.65mm*'}])
    newPart['name'].append('Sensor : ADE7763xRS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

