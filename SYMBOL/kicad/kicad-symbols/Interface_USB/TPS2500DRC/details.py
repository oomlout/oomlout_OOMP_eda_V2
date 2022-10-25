
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "TPS2500DRC"
    hexID = "SZKINTERFACEUTPS25DRC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS2500DRC', 'kicadSymbolFootprint': 'Package_SON:Texas_S-PVSON-N10', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps2500.pdf', 'kicadSymbolki_keywords': 'USB switch boost', 'kicadSymbolki_description': 'Integrated USB power Switch with Boost Converter, High-Efficiency Eco-mode Control Scheme, Texas S-PVSON-10', 'kicadSymbolki_fp_filters': 'Texas*S*PVSON*N10*'}])
    newPart['name'].append('Interface_USB : TPS2500DRC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

