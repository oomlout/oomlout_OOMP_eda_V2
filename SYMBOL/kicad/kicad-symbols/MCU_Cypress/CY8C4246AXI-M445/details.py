
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Cypress"
    oIndex = "CY8C4246AXI-M445"
    hexID = "SZKMCUCYPRESSCY8C4246AXIM445"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CY8C4245AXI-M445', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CY8C4246AXI-M445', 'kicadSymbolFootprint': 'Package_QFP:TQFP-64_14x14mm_P0.8mm', 'kicadSymbolDatasheet': 'https://www.cypress.com/file/139956/download', 'kicadSymbolki_keywords': 'Cypress Microcontroller Arm CapSense LCD', 'kicadSymbolki_description': 'PSoC 4200M series, 48MHz CPU, 64KB Flash, 8KB SRAM, 64-TQFP', 'kicadSymbolki_fp_filters': 'TQFP*14x14mm*P0.8mm*'}])
    newPart['name'].append('MCU_Cypress : CY8C4246AXI-M445')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

