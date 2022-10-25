
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "MCUU-QFN14-84-ATTINY-01-MCAT84QF14"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSMCUUQFN1484ATTINY1MCAT84QF14"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCUU-QFN14-84-ATTINY-01-MCAT84QF14', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:MCUU-QFN14-84-ATTINY-01-MCAT84QF14', 'kicadSymbolDatasheet': 'oom.lt/MCAT84QF14', 'kicadSymbolki_keywords': 'AVR 8bit Microcontroller tinyAVR', 'kicadSymbolki_description': 'hexID: MCAT84QF14;20MHz, 8kB Flash, 512B SRAM, 512B EEPROM, debugWIRE, QFN-20', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('oomlout_OOMP_parts : MCUU-QFN14-84-ATTINY-01-MCAT84QF14')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

