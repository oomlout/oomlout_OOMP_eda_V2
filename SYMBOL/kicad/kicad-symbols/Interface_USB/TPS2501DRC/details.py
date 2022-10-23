
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "TPS2501DRC"
    hexID = "SZKINTERFACEUTPS251DRC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS2500DRC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS2501DRC', 'kicadSymbolFootprint': 'Package_SON:Texas_S-PVSON-N10', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps2500.pdf', 'kicadSymbolki_keywords': 'USB switch boost', 'kicadSymbolki_description': 'Integrated USB power Switch with Boost Converter, Constant Frequency, Texas S-PVSON-10', 'kicadSymbolki_fp_filters': 'Texas*S*PVSON*N10*'}])
    newPart['name'].append('TPS2501DRC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

