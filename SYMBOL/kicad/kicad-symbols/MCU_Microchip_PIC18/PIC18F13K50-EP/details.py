
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_PIC18"
    oIndex = "PIC18F13K50-EP"
    hexID = "SZKMCUMCHIPPIC18PIC18F13K5EP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PIC18F13K50-EP', 'kicadSymbolFootprint': 'Package_DIP:DIP-20_W7.62mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/41350c.pdf', 'kicadSymbolki_keywords': 'Flash-Based 8bit CMOS Microcontroller XLP', 'kicadSymbolki_description': '8K Flash, 512 SRAM, 256 EEPROM, USB, nanoWatt XLP, DIP20', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* PDIP*W7.62mm*'}])
    newPart['name'].append('PIC18F13K50-EP')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

