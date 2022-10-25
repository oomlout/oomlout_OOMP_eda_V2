
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_SiliconLabs"
    oIndex = "C8051F383-GM"
    hexID = "SZKMCUSILICONLABSC851F383GM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'C8051F381-GM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'C8051F383-GM', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-32-1EP_5x5mm_P0.5mm_EP3.3x3.3mm', 'kicadSymbolDatasheet': 'https://www.silabs.com/documents/public/data-sheets/C8051F38x.pdf', 'kicadSymbolki_keywords': '8051 microcontroller PCA UART USB SPI I2C ADC QFN32', 'kicadSymbolki_description': 'Full Speed USB Flash MCU Family, 32k flash, 2304 ram, 25 IO, ADC, Temperature, VREF, QFN-32', 'kicadSymbolki_fp_filters': 'QFN*1EP*5x5mm*P0.5mm*'}])
    newPart['name'].append('MCU_SiliconLabs : C8051F383-GM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

