
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F1829-IST"
    hexID = "SZKMCUMCHIPPIC16PIC16F1829IST"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F1829-IP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F1829-IST', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41440C.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit CMOS Microcontroller Low Power', 'kicadSymbolki_description': 'Flash-Based, 8-Bit CMOS Microcontrollers, TSSOP', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*3.9x8.7mm*P1.27mm* TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F1829-IST')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

