
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_SiliconLabs"
    oIndex = "EFM8BB10F8G-A-SOIC16"
    hexID = "SZKMCUSILICONLABSEFM8BB1F8GASOIC16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EFM8BB10F8G-A-SOIC16', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/efm8bb1-datasheet.pdf', 'kicadSymbolki_keywords': '8051 microcontroller PWM UART SPI I2C ADC SOIC16', 'kicadSymbolki_description': '8051-compatible microcontroller, 25 MHz, 2.2 to 3.6V, 8K flash, 512B RAM, -40 to +85 C, SOIC16', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9mm*P1.27mm*'}])
    newPart['name'].append('EFM8BB10F8G-A-SOIC16')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

