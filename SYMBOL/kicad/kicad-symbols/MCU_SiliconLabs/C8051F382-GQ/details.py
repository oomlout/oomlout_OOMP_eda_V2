
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_SiliconLabs"
    oIndex = "C8051F382-GQ"
    hexID = "SZKMCUSILICONLABSC851F382GQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C8051F380-GQ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'C8051F382-GQ', 'kicadSymbolFootprint': 'Package_QFP:TQFP-48_7x7mm_P0.5mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/C8051F38x.pdf', 'kicadSymbolki_keywords': '8051 microcontroller PCA UART USB SPI I2C ADC EMIF TQFP48', 'kicadSymbolki_description': 'Full Speed USB Flash MCU Family, 32k flash, 2304 ram, 40 IO, EMIF, ADC, Temperature, VREF, TQFP-48', 'kicadSymbolki_fp_filters': 'TQFP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_SiliconLabs : C8051F382-GQ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

