
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F1459-ISO"
    hexID = "SZKMCUMCHIPPIC16PIC16F1459ISO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F1459-IP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F1459-ISO', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller Low Power', 'kicadSymbolki_description': 'PIC16F1454, 8192W FLASH, 1024B SRAM, PDIP-20', 'kicadSymbolki_fp_filters': 'DIP* PDIP* SO*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F1459-ISO')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

