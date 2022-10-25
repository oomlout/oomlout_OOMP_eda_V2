
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F1454-IST"
    hexID = "SZKMCUMCHIPPIC16PIC16F1454IST"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC16F1454-IP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F1454-IST', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller Low Power', 'kicadSymbolki_description': '8192W FLASH, 1024B SRAM, PDIP-14', 'kicadSymbolki_fp_filters': 'DIP* PDIP* SO*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F1454-IST')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

