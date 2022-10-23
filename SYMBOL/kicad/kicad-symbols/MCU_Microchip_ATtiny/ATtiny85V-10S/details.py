
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Microchip_ATtiny"
    oIndex = "ATtiny85V-10S"
    hexID = "SZKMCUMCHIPATTINYATTINY85V1S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ATtiny25V-10S', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATtiny85V-10S', 'kicadSymbolFootprint': 'Package_SO:SOIC-8W_5.3x5.3mm_P1.27mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/atmel-2586-avr-8-bit-microcontroller-attiny25-attiny45-attiny85_datasheet.pdf', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': '10MHz, 8kB Flash, 512B SRAM, 512B EEPROM, debugWIRE, SOIC-8W', 'kicadSymbolki_fp_filters': 'SOIC*5.3x5.3mm*P1.27mm*'}])
    newPart['name'].append('ATtiny85V-10S')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

