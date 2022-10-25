
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_SwitchedCapacitor"
    oIndex = "LM27762"
    hexID = "SZKREGULATORSWITCHEDCAPACITORLM27762"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM27762', 'kicadSymbolFootprint': 'Package_SON:WSON-12-1EP_3x2mm_P0.5mm_EP1x2.65_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm27762.pdf', 'kicadSymbolki_keywords': 'Low-noise inverting charge pump with both positive and negative LDOs', 'kicadSymbolki_description': 'Low-noise inverting charge pump with both positive and negative LDOs, with 2.7V-5.5V input to +1.5 to +5V and -1.5 to -5V Output Voltage, WSON-12', 'kicadSymbolki_fp_filters': 'WSON*1EP?3x2mm*P0.5mm*ThermalVias*'}])
    newPart['name'].append('Regulator_SwitchedCapacitor : LM27762')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

