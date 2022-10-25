
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Cypress"
    oIndex = "CY8C4247LQQ-BL483"
    hexID = "SZKMCUCYPRESSCY8C4247LQQBL483"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CY8C4xx7LQI-4xx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CY8C4247LQQ-BL483', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-56-1EP_7x7mm_P0.4mm_EP5.6x5.6mm', 'kicadSymbolDatasheet': 'http://www.cypress.com/file/137466/download', 'kicadSymbolki_keywords': 'CYPRESS PSOC BLE CY8 CY8C4 ARM CORTEX M0 BLUETOOTH QFN', 'kicadSymbolki_description': ' ENGR_SAMPLE,  56-QFN, 48-MHz ARM® Cortex®-M0, 128KB Flash, 16kB SRAM, NO UDB, CAP-SENSE W/ GESTURE, LCD DRIVE', 'kicadSymbolki_fp_filters': 'QFN*1EP*7x7mm*P0.4mm*'}])
    newPart['name'].append('MCU_Cypress : CY8C4247LQQ-BL483')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

