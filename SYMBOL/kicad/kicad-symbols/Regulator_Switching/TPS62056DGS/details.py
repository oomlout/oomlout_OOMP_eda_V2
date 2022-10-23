
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS62056DGS"
    hexID = "SZKREGULATORSWITCHINGTPS6256DGS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS62056DGS', 'kicadSymbolFootprint': 'Package_SO:VSSOP-10_3x3mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps62056.pdf', 'kicadSymbolki_keywords': 'voltage regulator switch mode step down', 'kicadSymbolki_description': '800 mA Step-Down Converter, Adjustable Output Voltage, 0.7-6V Input Voltage, VSSOP-10', 'kicadSymbolki_fp_filters': 'VSSOP*3x3mm*P0.5mm*'}])
    newPart['name'].append('TPS62056DGS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

