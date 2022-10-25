
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Cypress"
    oIndex = "CY8C4247AXI-M485"
    hexID = "SZKMCUCYPRESSCY8C4247AXIM485"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CY8C4245AXI-M445', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CY8C4247AXI-M485', 'kicadSymbolFootprint': 'Package_QFP:TQFP-64_14x14mm_P0.8mm', 'kicadSymbolDatasheet': 'https://www.cypress.com/file/139956/download', 'kicadSymbolki_keywords': 'Cypress Microcontroller Arm CapSense IDAC LCD CAN', 'kicadSymbolki_description': 'PSoC 4200M series, 48MHz CPU, 128KB Flash, 16KB SRAM, 64-TQFP', 'kicadSymbolki_fp_filters': 'TQFP*14x14mm*P0.8mm*'}])
    newPart['name'].append('MCU_Cypress : CY8C4247AXI-M485')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

