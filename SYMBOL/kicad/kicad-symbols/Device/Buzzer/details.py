
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Buzzer"
    hexID = "SZKDEVICEBUZZER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'BZ', 'kicadSymbolValue': 'Buzzer', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'quartz resonator ceramic', 'kicadSymbolki_description': 'Buzzer, polarized', 'kicadSymbolki_fp_filters': '*Buzzer*'}])
    newPart['name'].append('Device : Buzzer')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

