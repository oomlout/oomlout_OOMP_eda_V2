
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC16"
    oIndex = "PIC16F505-IP"
    hexID = "SZKMCUMCHIPPIC16PIC16F55IP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC16F505-IP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41236E.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8bit Microcontroller', 'kicadSymbolki_description': '1024W FLASH, 72B SRAM, DIP14', 'kicadSymbolki_fp_filters': 'PDIP* DIP*'}])
    newPart['name'].append('MCU_Microchip_PIC16 : PIC16F505-IP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

