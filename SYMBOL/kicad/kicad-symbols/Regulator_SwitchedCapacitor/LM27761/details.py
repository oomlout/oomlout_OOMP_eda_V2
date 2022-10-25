
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_SwitchedCapacitor"
    oIndex = "LM27761"
    hexID = "SZKREGULATORSWITCHEDCAPACITORLM27761"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM27761', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_2x2mm_P0.5mm_EP0.9x1.6mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm27761.pdf', 'kicadSymbolki_keywords': 'low-noise switched capacitor voltage converter invert', 'kicadSymbolki_description': 'low-noise regulated switched-capacitor voltage inverter with 2.7V-5.5V input to -1.5 to -5V Output Voltage, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*1EP?2x2mm*P0.5mm*'}])
    newPart['name'].append('Regulator_SwitchedCapacitor : LM27761')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

