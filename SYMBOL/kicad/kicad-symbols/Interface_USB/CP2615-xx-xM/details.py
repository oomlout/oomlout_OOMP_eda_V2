
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "CP2615-xx-xM"
    hexID = "SZKINTERFACEUCP2615XXXM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CP2615-xx-xM', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.3x3.3mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/cp2615-datasheet.pdf', 'kicadSymbolki_keywords': 'usb i2s i2c uart audio bridge hid gpio', 'kicadSymbolki_description': 'USB to I2S bridge, USB 1.0 Audio Class, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('Interface_USB : CP2615-xx-xM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

