
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F887-IP"
    hexID = "SZKMCUMCHIPPIC16PIC16F887IP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F884-IP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F887-IP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41291D.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit CMOS Microcontroller', 'kicadSymbolki_description': '8K Flash, 368B SRAM, 256B EEPROM, DIP40', 'kicadSymbolki_fp_filters': 'DIP* PDIP*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F887-IP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

