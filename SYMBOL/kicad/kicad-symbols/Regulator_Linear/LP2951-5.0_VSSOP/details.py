
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LP2951-5.0_VSSOP"
    hexID = "SZKREGULATORLINEARLP29515VSS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LP2951-3.0_VSSOP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LP2951-5.0_VSSOP', 'kicadSymbolFootprint': 'Package_SO:VSSOP-8_3.0x3.0mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lp2951.pdf', 'kicadSymbolki_keywords': 'Micropower Voltage Regulators with Shutdown', 'kicadSymbolki_description': 'Micropower Voltage Regulators with Shutdown, 100mA, Fixed Output 5.0V, LDO, VSSOP-8', 'kicadSymbolki_fp_filters': 'VSSOP*3.0x3.0mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Linear : LP2951-5.0_VSSOP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

