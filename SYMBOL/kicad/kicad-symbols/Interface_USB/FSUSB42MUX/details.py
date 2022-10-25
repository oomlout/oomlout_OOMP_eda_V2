
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "FSUSB42MUX"
    hexID = "SZKINTERFACEUFSU42MUX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FSUSB42MUX', 'kicadSymbolFootprint': 'Package_SO:MSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FSUSB42-D.PDF', 'kicadSymbolki_keywords': 'USB 2.0 UART High Speed Switch', 'kicadSymbolki_description': 'Low-Power, Two-Port, High-Speed, USB2.0 (480Mbps) or UART Switch, MSOP-10', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Interface_USB : FSUSB42MUX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

