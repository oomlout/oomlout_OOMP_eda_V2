
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_SiliconLabs"
    oIndex = "EFM8UB31F40G-A-QFN24"
    hexID = "SZKMCUSILICONLABSEFM8UB31F4GAQFN24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EFM8UB31F40G-A-QFN24', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-24-1EP_4x4mm_P0.5mm_EP2.6x2.6mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/efm8ub3-datasheet.pdf', 'kicadSymbolki_keywords': '8051 microcontroller PWM UART SPI I2C USB LDOREG ADC QFN24', 'kicadSymbolki_description': '8051-compatible microcontroller, 48 MHz, 2.3 to 5.5V, 40K flash, 3.25K RAM, -40 to +85 C, QFN-24', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('MCU_SiliconLabs : EFM8UB31F40G-A-QFN24')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

