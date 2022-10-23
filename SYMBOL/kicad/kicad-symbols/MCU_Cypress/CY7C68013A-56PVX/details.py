
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Cypress"
    oIndex = "CY7C68013A-56PVX"
    hexID = "SZKMCUCYPRESSCY7C6813A56PVX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CY7C68013A-56PVX', 'kicadSymbolFootprint': 'Package_SO:SSOP-56_7.5x18.5mm_P0.635mm', 'kicadSymbolDatasheet': 'http://www.cypress.com/file/138911/download', 'kicadSymbolki_keywords': 'FX2LP 8-bit USB MCU', 'kicadSymbolki_description': 'CYPRESS FX2LP USB Microcontroller, 48MHz 8051, 16KB RAM, USB 2.0, I2C, SSOP-56', 'kicadSymbolki_fp_filters': 'SSOP*7.5x18.5mm*P0.635mm*'}])
    newPart['name'].append('CY7C68013A-56PVX')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

