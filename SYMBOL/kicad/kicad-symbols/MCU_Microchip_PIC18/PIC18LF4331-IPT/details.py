
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18LF4331-IPT"
    hexID = "SZKMCUMCHIPPIC18PIC18LF4331IPT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F4331-IPT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18LF4331-IPT', 'kicadSymbolFootprint': 'Package_QFP:TQFP-44_10x10mm_P0.8mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/39616d.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8-Bit Microcontroller XLP', 'kicadSymbolki_description': '8K Flash, 768B SRAM, 256B EEPROM, nanoWatt XLP, ADC, PWM, TQFP44', 'kicadSymbolki_fp_filters': 'TQFP*10x10mm*P0.8mm*'}])
    newPart['name'].append('MCU_Microchip_PIC18 : PIC18LF4331-IPT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

