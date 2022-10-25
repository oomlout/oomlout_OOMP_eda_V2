
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas"
    oIndex = "LM4F111B2QR"
    hexID = "SZKMCUTEXASLM4F111B2QR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TM4C1230C3PM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4F111B2QR', 'kicadSymbolFootprint': 'Package_QFP:LQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tm4c1230c3pm.pdf', 'kicadSymbolki_keywords': 'ARM Stellaris Cortex M4 MCU NRND', 'kicadSymbolki_description': 'Replaced by TM4C1230C3PM, LQFP64', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.5mm*'}])
    newPart['name'].append('MCU_Texas : LM4F111B2QR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

