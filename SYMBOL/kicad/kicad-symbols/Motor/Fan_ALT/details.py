
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Motor"
    oIndex = "Fan_ALT"
    hexID = "SZKMOTORFANALT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'M', 'kicadSymbolValue': 'Fan_ALT', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'Fan Motor', 'kicadSymbolki_description': 'Fan without PWM or tach, alternative symbol', 'kicadSymbolki_fp_filters': 'PinHeader*P2.54mm* TerminalBlock*'}])
    newPart['name'].append('Motor : Fan_ALT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

