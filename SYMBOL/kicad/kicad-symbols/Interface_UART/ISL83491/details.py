
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_UART"
    oIndex = "ISL83491"
    hexID = "SZKINTERFACEUARTISL83491"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ISL83491', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.intersil.com/content/dam/Intersil/documents/isl8/isl83483-85-88-90-91.pdf', 'kicadSymbolki_keywords': 'RS485 RS422 transceiver full duplex', 'kicadSymbolki_description': '10Mbps RS485/RS422 transceiver, full duplex, receiver/driver enable, low power shutdown', 'kicadSymbolki_fp_filters': 'SOIC* DIP*W7.62mm*'}])
    newPart['name'].append('Interface_UART : ISL83491')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

