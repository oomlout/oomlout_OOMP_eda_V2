
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Cypress"
    oIndex = "CYBL10162-56LQXI"
    hexID = "SZKMCUCYPRESSCYBL116256LQXI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CYBL10x6x-56LQxx', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CYBL10162-56LQXI', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-56-1EP_7x7mm_P0.4mm_EP5.6x5.6mm', 'kicadSymbolDatasheet': 'http://www.cypress.com/documentation/datasheets/cybl10x6x-family-datasheet-programmable-radio-chip-bluetooth-low-energy', 'kicadSymbolki_keywords': 'CYPRESS PROC BLE CY8BL ARM CORTEX M0 BLUETOOTH QFN', 'kicadSymbolki_description': '56-QFN, 48-MHz ARM® Cortex®-M0, 128KB Flash, 16kB SRAM, BLE 4.1, NO CAP-SENSE, 2 SCB, 4 TCPWM, NO I2S, 4 PWM , NO LCD, 1MSPS 12-BIT SAR', 'kicadSymbolki_fp_filters': 'QFN*1EP*7x7mm*P0.4mm*'}])
    newPart['name'].append('MCU_Cypress : CYBL10162-56LQXI')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

