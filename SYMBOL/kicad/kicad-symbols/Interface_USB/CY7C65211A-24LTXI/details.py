
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "CY7C65211A-24LTXI"
    hexID = "SZKINTERFACEUCY7C65211A24LTXI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CY7C65211-24LTXI', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CY7C65211A-24LTXI', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm', 'kicadSymbolDatasheet': 'http://www.cypress.com/file/139886/download', 'kicadSymbolki_keywords': 'USB-Serial single channel bridge', 'kicadSymbolki_description': 'USB-Serial single channel bridge with capsense and BCD, +1.71V to +5.5V VDD, UART/I2C/SPI/RS232/RS422/RS485, QFN-24', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('Interface_USB : CY7C65211A-24LTXI')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

