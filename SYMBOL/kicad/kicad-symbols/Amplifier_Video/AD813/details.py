
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Video"
    oIndex = "AD813"
    hexID = "SZKAMPLIFIERVIDEOAD813"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD813', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD813.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'triple opamp', 'kicadSymbolki_description': 'Single Supply, Low Power, Triple Video Amplifier, DIP-14/SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('AD813')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

