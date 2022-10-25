
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Cypress"
    oIndex = "CY7C68014A-56LTX"
    hexID = "SZKMCUCYPRESSCY7C6814A56LTX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CY7C68013A-56LTX', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CY7C68014A-56LTX', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-56-1EP_8x8mm_P0.5mm_EP4.5x5.2mm_ThermalVias_TopTented', 'kicadSymbolDatasheet': 'http://www.cypress.com/file/138911/download', 'kicadSymbolki_keywords': 'FX2LP 8-bit USB MCU', 'kicadSymbolki_description': 'CYPRESS FX2LP USB Microcontroller, 48MHz 8051, 16KB RAM, USB 2.0, I2C, QFN-56', 'kicadSymbolki_fp_filters': 'QFN*1EP*8x8mm*P0.5mm*'}])
    newPart['name'].append('MCU_Cypress : CY7C68014A-56LTX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

