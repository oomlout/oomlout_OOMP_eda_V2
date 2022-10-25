
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F871-IL"
    hexID = "SZKMCUMCHIPPIC16PIC16F871IL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F871-IL', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/30569b.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit CMOS Microcontroller', 'kicadSymbolki_description': '2K Flash, 128B SRAM, 64B EEPROM, PLCC44', 'kicadSymbolki_fp_filters': 'PLCC*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F871-IL')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

