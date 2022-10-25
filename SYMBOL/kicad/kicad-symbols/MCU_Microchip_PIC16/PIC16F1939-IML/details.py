
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F1939-IML"
    hexID = "SZKMCUMCHIPPIC16PIC16F1939IML"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F1934-IML', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F1939-IML', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41364E.pdf', 'kicadSymbolki_description': 'PIC16F193XLF193X - Flash-Based, 8-Bit CMOS Microcontrollers, QFN-44', 'kicadSymbolki_fp_filters': 'MLF*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F1939-IML')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

