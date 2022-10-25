
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F84-XXP"
    hexID = "SZKMCUMCHIPPIC16PIC16F84XXP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F83-XXP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F84-XXP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/30430c.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit Microcontroller', 'kicadSymbolki_description': 'PIC16F84, 1K Flash, 68B SRAM, 64B EEPROM, DIP18', 'kicadSymbolki_fp_filters': 'DIP* PDIP*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F84-XXP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

