
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_SiliconLabs"
    oIndex = "EFM8UB31F40G-A-QSOP24"
    hexID = "SZKMCUSILICONLABSEFM8UB31F4GAQS24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EFM8UB31F40G-A-QSOP24', 'kicadSymbolFootprint': 'Package_SO:QSOP-24_3.9x8.7mm_P0.635mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/efm8ub3-datasheet.pdf', 'kicadSymbolki_keywords': '8051 microcontroller PWM UART SPI I2C USB LDOREG ADC QSOP24', 'kicadSymbolki_description': '8051-compatible microcontroller, 48 MHz, 2.3 to 5.5V, 40K flash, 3.25K RAM, -40 to +85 C, QSOP-24', 'kicadSymbolki_fp_filters': 'QSOP*3.9x8.7mm*P0.635mm*'}])
    newPart['name'].append('EFM8UB31F40G-A-QSOP24')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

