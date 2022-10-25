
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "AM26LS31xNS"
    hexID = "SZKINTERFACEAM26LS31XNS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AM26LS31CD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AM26LS31xNS', 'kicadSymbolFootprint': 'Package_SO:SO-16_5.3x10.2mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/am26ls31.pdf', 'kicadSymbolki_keywords': 'driver rs485 rs422 differential', 'kicadSymbolki_description': '32Mbps 3.3V RS485 Quad Line Drivers, SO-16', 'kicadSymbolki_fp_filters': 'SO*5.3x10.2mm*P1.27mm*'}])
    newPart['name'].append('Interface : AM26LS31xNS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

