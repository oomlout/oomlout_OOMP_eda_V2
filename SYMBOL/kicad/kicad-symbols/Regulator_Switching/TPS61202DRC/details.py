
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS61202DRC"
    hexID = "SZKREGULATORSWITCHINGTPS6122DRC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS61200DRC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS61202DRC', 'kicadSymbolFootprint': 'Package_SON:Texas_S-PVSON-N10_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps61200.pdf', 'kicadSymbolki_keywords': 'boost step-up DC/DC synchronous', 'kicadSymbolki_description': 'Low Input Voltage Synchronous Boost Converter With 1.3A Switches, Fixed 5V Output Voltage, 0.3-5.5V Input Voltage, VSON-10', 'kicadSymbolki_fp_filters': 'Texas*S*PVSON*N10*ThermalVias*'}])
    newPart['name'].append('TPS61202DRC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

