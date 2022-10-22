
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "MBR0540"
    hexID = "SZKDIODEMBR54"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BAT48ZFILM', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'MBR0540', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-123', 'kicadSymbolDatasheet': 'http://www.mccsemi.com/up_pdf/MBR0520~MBR0580(SOD123).pdf', 'kicadSymbolki_keywords': 'diode Schottky', 'kicadSymbolki_description': '40V 0.5A Schottky Power Rectifier Diode, SOD-123', 'kicadSymbolki_fp_filters': 'D*SOD?123*'}])
    newPart['name'].append('MBR0540')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

