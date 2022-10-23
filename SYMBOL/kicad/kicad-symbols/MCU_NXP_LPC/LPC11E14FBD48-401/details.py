
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_NXP_LPC"
    oIndex = "LPC11E14FBD48-401"
    hexID = "SZKMCUNXPLPCLPC11E14FBD4841"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LPC11E12FBD48-201', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LPC11E14FBD48-401', 'kicadSymbolFootprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/LPC11U1X.pdf', 'kicadSymbolki_keywords': 'nxp lpc arm microcontroller cortex', 'kicadSymbolki_description': 'LPC11U00 USB series, 50MHz Cortex-M0 MCU, USB, ADC, USART, I2C, SPI, LQFP48 package', 'kicadSymbolki_fp_filters': '*QFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('LPC11E14FBD48-401')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

