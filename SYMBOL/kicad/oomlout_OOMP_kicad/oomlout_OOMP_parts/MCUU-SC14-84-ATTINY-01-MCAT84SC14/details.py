
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "MCUU-SC14-84-ATTINY-01-MCAT84SC14"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSMCUUSC1484ATTINY1MCAT84SC14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCUU-SC14-84-ATTINY-01-MCAT84SC14', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:MCUU-SC14-84-ATTINY-01-MCAT84SC14', 'kicadSymbolDatasheet': 'oom.lt/MCAT84SC14', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': 'hexID: MCAT84SC14;12MHz, 2kB Flash, 128B SRAM, No EEPROM, SOIC-14', 'kicadSymbolki_fp_filters': 'SOIC*3.9x8.7mm*P1.27mm*'}])
    newPart['name'].append('MCUU-SC14-84-ATTINY-01-MCAT84SC14')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

