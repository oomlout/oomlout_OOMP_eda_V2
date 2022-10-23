
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_LPC"
    oIndex = "LPC11E12FBD48-201"
    hexID = "SZKMCUNXPLPCLPC11E12FBD4821"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LPC11E12FBD48-201', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/LPC11E1X.pdf', 'kicadSymbolki_keywords': 'nxp lpc arm microcontroller cortex', 'kicadSymbolki_description': 'LPC11E1x, 50MHz Cortex-M0 MCU, 16kB Flash, 1kB EEPROM, 6kB SRAM, USART, I2C, SSP, ADC, Power Profile, LQFP48', 'kicadSymbolki_fp_filters': '*QFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('LPC11E12FBD48-201')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

