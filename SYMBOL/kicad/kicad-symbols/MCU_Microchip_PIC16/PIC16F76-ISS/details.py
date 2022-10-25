
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F76-ISS"
    hexID = "SZKMCUMCHIPPIC16PIC16F76ISS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F73-ISS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F76-ISS', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/30325b.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit Microcontroller', 'kicadSymbolki_description': 'PIC16F76, 8K Flash, 368B SRAM, ADC, PWM, SSOP28', 'kicadSymbolki_fp_filters': 'SSOP*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F76-ISS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

