
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS7A7200RGW"
    hexID = "SZKREGULATORLINEARTPS7A72RGW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS7A7200RGW', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PVQFN-N20_EP3.15x3.15mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps7a7200.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo voltage', 'kicadSymbolki_description': '2A, Low-Dropout Voltage Regulator, 1.5-6.5V Input, Adjustable 0.9-5V Output, VQFN-20', 'kicadSymbolki_fp_filters': 'Texas*S?PVQFN*'}])
    newPart['name'].append('Regulator_Linear : TPS7A7200RGW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

