
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LMG3410"
    hexID = "SZKPOWERMANAGEMENTLMG341"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'LMG3410', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_RWH0032A_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/snosd10c/snosd10c.pdf', 'kicadSymbolki_keywords': 'N-Channel GaN MOSFET', 'kicadSymbolki_description': '600-V 12-A Integrated GaN Power Stage, RWH0032A', 'kicadSymbolki_fp_filters': 'Texas*RWH0032A*'}])
    newPart['name'].append('LMG3410')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

