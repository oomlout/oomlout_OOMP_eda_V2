
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Supervisor"
    oIndex = "TL7705ACPSR"
    hexID = "SZKPOWERSUPERVISORTL775ACPSR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TL7705ACPSR', 'kicadSymbolFootprint': 'Package_SO:SO-8_5.3x6.2mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com.cn/cn/lit/ds/symlink/tl7705a.pdf', 'kicadSymbolki_keywords': 'voltage supervisor', 'kicadSymbolki_description': 'Supply-Voltage Supervisors, 4.55V, SO-8', 'kicadSymbolki_fp_filters': 'SO*5.3x6.2mm*P1.27mm*'}])
    newPart['name'].append('TL7705ACPSR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

