
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS51200DRC"
    hexID = "SZKREGULATORLINEARTPS512DRC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS51200DRC', 'kicadSymbolFootprint': 'Package_SON:VSON-10-1EP_3x3mm_P0.5mm_EP1.65x2.4mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps51200.pdf', 'kicadSymbolki_keywords': 'DDR LDO', 'kicadSymbolki_description': 'Sink and Source DDR Termination Regulator, VSON-10', 'kicadSymbolki_fp_filters': '*VSON?10?1EP?3x3mm?P0.5mm*'}])
    newPart['name'].append('Regulator_Linear : TPS51200DRC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

