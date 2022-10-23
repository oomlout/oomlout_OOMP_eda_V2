
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18LF13K50-ESO"
    hexID = "SZKMCUMCHIPPIC18PIC18LF13K5ESO"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PIC18F13K50-ESO', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18LF13K50-ESO', 'kicadSymbolFootprint': 'Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/41350c.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8bit CMOS Microcontroller XLP', 'kicadSymbolki_description': '8K Flash, 512 SRAM, 256 EEPROM, USB, nanoWatt XLP, SOIC20', 'kicadSymbolki_fp_filters': 'SOIC*W*7.5x12.8mm*P1.27mm*'}])
    newPart['name'].append('PIC18LF13K50-ESO')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

