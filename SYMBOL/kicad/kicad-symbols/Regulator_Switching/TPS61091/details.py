
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS61091"
    hexID = "SZKREGULATORSWITCHINGTPS6191"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS61090', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS61091', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PVQFN-N16_EP2.7x2.7mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps61090.pdf', 'kicadSymbolki_keywords': 'Fixed 3.3V 2A battery boost converter', 'kicadSymbolki_description': '2A Step-Up DC-DC Converter for Batteries, Isw up to 2500mA, 3.3V Output Voltage, QFN-16', 'kicadSymbolki_fp_filters': 'Texas*S?PVQFN?N*'}])
    newPart['name'].append('TPS61091')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

