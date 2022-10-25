
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Cypress"
    oIndex = "CYBL10x6x-56LQxx"
    hexID = "SZKMCUCYPRESSCYBL1X6X56LQXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CYBL10x6x-56LQxx', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-56-1EP_7x7mm_P0.4mm_EP5.6x5.6mm', 'kicadSymbolDatasheet': 'http://www.cypress.com/documentation/datasheets/cybl10x6x-family-datasheet-programmable-radio-chip-bluetooth-low-energy', 'kicadSymbolki_keywords': 'CYPRESS PROC BLE CY8BL ARM CORTEX M0 BLUETOOTH QFN', 'kicadSymbolki_description': 'Programmable Radio-on-Chip With Bluetooth Low Energy, 48-MHz ARM® Cortex®-M0 , 56-QFN', 'kicadSymbolki_fp_filters': 'QFN*1EP*7x7mm*P0.4mm*'}])
    newPart['name'].append('MCU_Cypress : CYBL10x6x-56LQxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

