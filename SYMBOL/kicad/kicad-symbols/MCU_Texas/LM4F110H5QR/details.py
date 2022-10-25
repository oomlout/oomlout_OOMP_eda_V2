
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas"
    oIndex = "LM4F110H5QR"
    hexID = "SZKMCUTEXASLM4F11H5QR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TM4C1231C3PM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4F110H5QR', 'kicadSymbolFootprint': 'Package_QFP:LQFP-64_10x10mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tm4c1231h6pm.pdf', 'kicadSymbolki_keywords': 'ARM Stellaris Cortex M4 MCU NRND', 'kicadSymbolki_description': 'Replaced by TM4C1231H6PM, LQFP64', 'kicadSymbolki_fp_filters': 'LQFP*10x10mm*P0.5*'}])
    newPart['name'].append('MCU_Texas : LM4F110H5QR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

