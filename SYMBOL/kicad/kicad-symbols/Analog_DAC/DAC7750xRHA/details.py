
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "DAC7750xRHA"
    hexID = "SZKANALOGDACDAC775XRHA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DAC8750xRHA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DAC7750xRHA', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PVQFN-N40_EP4.6x4.6mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/dac7750.pdf', 'kicadSymbolki_keywords': 'DAC Current Loop 20mA', 'kicadSymbolki_description': 'Single-Channel, 12bit Programmable Current Output DAC for 4-mA to 20-mA Current Loop Applications, VQFN-40', 'kicadSymbolki_fp_filters': 'Texas*PVQFN*'}])
    newPart['name'].append('Analog_DAC : DAC7750xRHA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

