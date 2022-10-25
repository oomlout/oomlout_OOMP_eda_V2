
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC12"
    oIndex = "PIC12LF1840T48-IST"
    hexID = "SZKMCUMCHIPPIC12PIC12LF184T48IST"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC12LF1840T48-IST', 'kicadSymbolFootprint': 'Package_SO:TSSOP-14_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/41594B.pdf', 'kicadSymbolki_keywords': 'FLASH-Based 8-Bit CMOS Microcontroller XLP RF Transmitter', 'kicadSymbolki_description': 'PIC12LF1840T48, 4kW FLASH, 256B SRAM, 256B EEPROM, RF, TSSOP14', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('MCU_Microchip_PIC12 : PIC12LF1840T48-IST')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

