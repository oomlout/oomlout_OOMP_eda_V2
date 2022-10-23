
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_SiliconLabs"
    oIndex = "EFM8UB30F40G-A-QFN20"
    hexID = "SZKMCUSILICONLABSEFM8UB3F4GAQFN2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EFM8UB30F40G-A-QFN20', 'kicadSymbolFootprint': 'Package_DFN_QFN:SiliconLabs_QFN-20-1EP_3x3mm_P0.5mm_EP1.8x1.8mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/efm8ub3-datasheet.pdf', 'kicadSymbolki_keywords': '8051 microcontroller PWM UART SPI I2C USB LDOREG ADC QFN20', 'kicadSymbolki_description': '8051-compatible microcontroller, 48 MHz, 2.3 to 5.5V, 40K flash, 3.25K RAM, -40 to +85 C, QFN-20', 'kicadSymbolki_fp_filters': 'SiliconLabs*QFN*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('EFM8UB30F40G-A-QFN20')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

