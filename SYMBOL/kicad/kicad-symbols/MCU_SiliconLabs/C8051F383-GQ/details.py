
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_SiliconLabs"
    oIndex = "C8051F383-GQ"
    hexID = "SZKMCUSILICONLABSC851F383GQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C8051F381-GQ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'C8051F383-GQ', 'kicadSymbolFootprint': 'Package_QFP:LQFP-32_7x7mm_P0.8mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/C8051F38x.pdf', 'kicadSymbolki_keywords': '8051 microcontroller PCA UART USB SPI I2C ADC LQFP32', 'kicadSymbolki_description': 'Full Speed USB Flash MCU Family, 32k flash, 2304 ram, 25 IO, ADC, Temperature, VREF, LQFP-32', 'kicadSymbolki_fp_filters': 'LQFP*7x7mm*P0.8mm*'}])
    newPart['name'].append('MCU_SiliconLabs : C8051F383-GQ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

