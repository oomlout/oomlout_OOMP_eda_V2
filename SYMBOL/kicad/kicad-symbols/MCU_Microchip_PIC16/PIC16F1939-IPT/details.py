
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F1939-IPT"
    hexID = "SZKMCUMCHIPPIC16PIC16F1939IPT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F1934-IPT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F1939-IPT', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41364E.pdf', 'kicadSymbolki_description': 'PIC16F193XLF193X - Flash-Based, 8-Bit CMOS Microcontrollers, TQFP-44', 'kicadSymbolki_fp_filters': 'TQFP*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F1939-IPT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

