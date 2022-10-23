
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas"
    oIndex = "MSP432E401Y"
    hexID = "SZKMCUTEXASMSP432E41Y"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP432E401Y', 'kicadSymbolFootprint': 'Package_QFP:LQFP-128_14x14mm_P0.4mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp432e401y.pdf', 'kicadSymbolki_keywords': 'ARM Cortex-M4F MSP432 MSP432E4 MSP432E401', 'kicadSymbolki_description': 'ARM Cortex-M4F MCU, 1024KB flash, 256KB RAM, 6KB EEPROM, 120MHz, 3.0-3.6V, TQFP-128', 'kicadSymbolki_fp_filters': 'LQFP*14x14mm*P0.4mm*'}])
    newPart['name'].append('MSP432E401Y')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

