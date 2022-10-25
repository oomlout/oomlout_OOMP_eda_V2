
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Transformer_SP_1S"
    hexID = "SZKDEVICETRSP1S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'T', 'kicadSymbolValue': 'Transformer_SP_1S', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'transformer coil magnet', 'kicadSymbolki_description': 'Transformer, split primary, single secondary'}])
    newPart['name'].append('Device : Transformer_SP_1S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

