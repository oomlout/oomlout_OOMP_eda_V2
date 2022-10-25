
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC10"
    oIndex = "PIC10F322-IOT"
    hexID = "SZKMCUMCHIPPIC1PIC1F322IOT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC10F320-IOT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC10F322-IOT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41585A.pdf', 'kicadSymbolki_keywords': 'FLASH 8-Bit CMOS Microcontroller', 'kicadSymbolki_description': '512W Flash, 64B SRAM, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT*23*6*'}])
    newPart['name'].append('MCU_Microchip_PIC10 : PIC10F322-IOT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

