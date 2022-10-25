
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F1220-SO"
    hexID = "SZKMCUMCHIPPIC18PIC18F122SO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F1220-SO', 'kicadSymbolFootprint': 'Package_SO:SOIC-18W_7.5x11.6mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39605F.pdf', 'kicadSymbolki_keywords': 'RAM ADC UART PWM', 'kicadSymbolki_description': '18-Pin Flash Microcontroller 4K Flash 256byte RAM', 'kicadSymbolki_fp_filters': 'SOIC*W*7.5x11.6mm*P1.27mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18F1220-SO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

