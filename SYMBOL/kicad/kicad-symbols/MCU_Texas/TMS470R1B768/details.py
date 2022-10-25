
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas"
    oIndex = "TMS470R1B768"
    hexID = "SZKMCUTEXASTMS47R1B768"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMS470R1B768', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tms470r1b768.pdf', 'kicadSymbolki_keywords': 'ARM 7TDM uC TMS470', 'kicadSymbolki_description': 'ARM7TDM Microcontroller, 768KB Flash, 48KB RAM, PQFP-144', 'kicadSymbolki_fp_filters': 'PQFP-144*'}])
    newPart['name'].append('MCU_Texas : TMS470R1B768')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

