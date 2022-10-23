
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS54336ADDA"
    hexID = "SZKREGULATORSWITCHINGTPS54336ADDA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS54336ADDA', 'kicadSymbolFootprint': 'Package_SO:TI_SO-PowerPAD-8_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps54336a.pdf', 'kicadSymbolki_keywords': 'Step-Down DC-DC Switching Regulator', 'kicadSymbolki_description': ' 4.5V to 28V Input, 3A, Synchronous Step-Down Converter with Eco-mode(tm)', 'kicadSymbolki_fp_filters': 'TI*SO*PowerPAD*ThermalVias*'}])
    newPart['name'].append('TPS54336ADDA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

