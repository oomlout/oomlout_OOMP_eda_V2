
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Cypress"
    oIndex = "CYBL10563-68FNXIT"
    hexID = "SZKMCUCYPRESSCYBL156368FNXIT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CYBL10563-68FNXIT', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.cypress.com/documentation/datasheets/cybl10x6x-family-datasheet-programmable-radio-chip-bluetooth-low-energy', 'kicadSymbolki_keywords': 'CYPRESS PROC BLE CY8BL ARM CORTEX M0 BLUETOOTH WLCSP', 'kicadSymbolki_description': '68-WLCSP, 48-MHz ARM® Cortex®-M0, 128KB Flash, 16kB SRAM, BLE 4.1, CAP-SENSE W/ GESTURES, 2 SCB, 4 TCPWM, I2S, 1 PWM , LCD, 1MSPS 12-BIT SAR', 'kicadSymbolki_fp_filters': 'WLCSP*'}])
    newPart['name'].append('MCU_Cypress : CYBL10563-68FNXIT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

