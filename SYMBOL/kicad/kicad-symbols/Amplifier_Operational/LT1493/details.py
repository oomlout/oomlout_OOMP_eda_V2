
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LT1493"
    hexID = "SZKAMPLIFIEROPERATIONALLT1493"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC6082xGN', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1493', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/14923f.pdf', 'kicadSymbolki_keywords': 'quad opamp', 'kicadSymbolki_description': '5MHz, 3V/µs, Low Power, Single Supply, Quad Precision Op Amps, SOIC-16', 'kicadSymbolki_fp_filters': 'SSOP*3.9x4.9mm*P0.635mm* SOIC*3.9x9.9mm*P1.27mm* QSOP*3.9x4.9mm*P0.635mm*'}])
    newPart['name'].append('LT1493')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

