
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface"
    oIndex = "AM26LS31CDB"
    hexID = "SZKINTERFACEAM26LS31CDB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AM26LS31CD', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AM26LS31CDB', 'kicadSymbolFootprint': 'Package_SO:SSOP-16_5.3x6.2mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/am26ls31.pdf', 'kicadSymbolki_keywords': 'driver rs485 rs422 differential', 'kicadSymbolki_description': '32Mbps 3.3V RS485 Quad Line Drivers, SSOP-16', 'kicadSymbolki_fp_filters': 'SSOP*5.3x6.2mm*P0.65mm*'}])
    newPart['name'].append('Interface : AM26LS31CDB')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

