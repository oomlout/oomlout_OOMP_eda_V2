
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS61090"
    hexID = "SZKREGULATORSWITCHINGTPS619"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS61090', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PVQFN-N16_EP2.7x2.7mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps61090.pdf', 'kicadSymbolki_keywords': 'Adjustable 2A battery boost converter', 'kicadSymbolki_description': '2A Step-Up DC-DC Converter for Batteries, Isw up to 2500mA, Adjustable output voltage, QFN-16', 'kicadSymbolki_fp_filters': 'Texas*S?PVQFN?N*'}])
    newPart['name'].append('Regulator_Switching : TPS61090')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

