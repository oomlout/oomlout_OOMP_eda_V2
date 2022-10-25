
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "GDT_2Pin"
    hexID = "SZKDEVICEGDT2PIN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'GD', 'kicadSymbolValue': 'GDT_2Pin', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'gdt', 'kicadSymbolki_description': 'Gas Discharge Tube with 2 Pins'}])
    newPart['name'].append('Device : GDT_2Pin')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

