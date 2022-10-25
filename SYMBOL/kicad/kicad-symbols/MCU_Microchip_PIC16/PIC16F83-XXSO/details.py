
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F83-XXSO"
    hexID = "SZKMCUMCHIPPIC16PIC16F83XXSO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F83-XXSO', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/30430c.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit Microcontroller', 'kicadSymbolki_description': 'PIC16F83, 512B Flash, 36B SRAM, 64B EEPROM, SOIC18', 'kicadSymbolki_fp_filters': 'SO*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F83-XXSO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

