
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS70451"
    hexID = "SZKREGULATORLINEARTPS7451"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS70402', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS70451', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-24-1EP_4.4x7.8mm_P0.65mm_EP3.4x7.8mm_Mask2.4x4.68mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps704.pdf', 'kicadSymbolki_keywords': 'dual ldo regulator', 'kicadSymbolki_description': 'Dual-Output, Low Dropout Voltage Regulators With Integrated SVS For Split Voltage Systems, Independent Enable, 3.3V 1A/1.8V 2A, HTSSOP-24', 'kicadSymbolki_fp_filters': 'HTSSOP*4.4x7.8mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Linear : TPS70451')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

