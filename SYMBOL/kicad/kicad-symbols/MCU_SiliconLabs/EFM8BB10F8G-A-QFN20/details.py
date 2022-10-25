
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_SiliconLabs"
    oIndex = "EFM8BB10F8G-A-QFN20"
    hexID = "SZKMCUSILICONLABSEFM8BB1F8GAQFN2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EFM8BB10F8G-A-QFN20', 'kicadSymbolFootprint': 'Package_DFN_QFN:SiliconLabs_QFN-20-1EP_3x3mm_P0.5mm_EP1.8x1.8mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/efm8bb1-datasheet.pdf', 'kicadSymbolki_keywords': '8051 microcontroller PWM UART SPI I2C ADC QFN20', 'kicadSymbolki_description': '8051-compatible microcontroller, 25 MHz, 2.2 to 3.6V, 8K flash, 512B RAM, -40 to +85 C, QFN20', 'kicadSymbolki_fp_filters': 'SiliconLabs*QFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('MCU_SiliconLabs : EFM8BB10F8G-A-QFN20')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

