
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_SiliconLabs"
    oIndex = "EFM8BB10F8G-A-QSOP24"
    hexID = "SZKMCUSILICONLABSEFM8BB1F8GAQS24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EFM8BB10F8G-A-QSOP24', 'kicadSymbolFootprint': 'Package_SO:QSOP-24_3.9x8.7mm_P0.635mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/efm8bb1-datasheet.pdf', 'kicadSymbolki_keywords': '8051 microcontroller PWM UART SPI I2C ADC QSOP24', 'kicadSymbolki_description': '8051-compatible microcontroller, 25 MHz, 2.2 to 3.6V, 8K flash, 512B RAM, -40 to +85 C, QSOP24', 'kicadSymbolki_fp_filters': 'QSOP*P0.635mm*'}])
    newPart['name'].append('MCU_SiliconLabs : EFM8BB10F8G-A-QSOP24')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

