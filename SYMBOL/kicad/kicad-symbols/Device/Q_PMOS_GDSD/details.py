
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Q_PMOS_GDSD"
    hexID = "SZKDEVICEQPMOSGDSD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'Q_PMOS_GDSD', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'transistor PMOS P-MOS P-MOSFET', 'kicadSymbolki_description': 'P-MOSFET transistor, gate/drain/source, drain connected to mounting plane'}])
    newPart['name'].append('Device : Q_PMOS_GDSD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

