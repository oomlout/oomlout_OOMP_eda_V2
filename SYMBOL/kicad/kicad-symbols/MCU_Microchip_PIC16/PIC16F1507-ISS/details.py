
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F1507-ISS"
    hexID = "SZKMCUMCHIPPIC16PIC16F157ISS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F1507-IP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F1507-ISS', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41586A.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller Low Power', 'kicadSymbolki_description': 'PIC16F1507, 2048W FLASH, 128B SRAM, SSOP-20', 'kicadSymbolki_fp_filters': 'DIP* PDIP* SO* SSOP*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F1507-ISS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

