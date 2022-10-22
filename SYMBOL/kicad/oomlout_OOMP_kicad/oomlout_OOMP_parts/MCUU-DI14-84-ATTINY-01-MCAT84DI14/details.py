
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "MCUU-DI14-84-ATTINY-01-MCAT84DI14"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSMCUUDI1484ATTINY1MCAT84DI14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCUU-DI14-84-ATTINY-01-MCAT84DI14', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:MCUU-DI14-84-ATTINY-01-MCAT84DI14', 'kicadSymbolDatasheet': 'oom.lt/MCAT84DI14', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': 'hexID: MCAT84DI14;20MHz, 8kB Flash, 512B SRAM, 512B EEPROM, debugWIRE, DIP-14', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('MCUU-DI14-84-ATTINY-01-MCAT84DI14')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

