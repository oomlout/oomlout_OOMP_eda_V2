
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas"
    oIndex = "TM4C1230H6PM"
    hexID = "SZKMCUTEXASTM4C123H6PM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TM4C1230C3PM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TM4C1230H6PM', 'kicadSymbolFootprint': 'Package_QFP:LQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tm4c1230h6pm.pdf', 'kicadSymbolki_keywords': 'ARM Tiva Cortex M4 MCU', 'kicadSymbolki_description': 'Tiva ARM 32bit CortexM4 Microcotroller, 80MHz, 256kB Flash, 32kB SRAM, 2k EEPROM, LQFP64', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('TM4C1230H6PM')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

