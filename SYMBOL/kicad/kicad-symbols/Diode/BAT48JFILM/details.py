
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BAT48JFILM"
    hexID = "SZKDIODEBAT48JFILM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BAT48JFILM', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-323', 'kicadSymbolDatasheet': 'www.st.com/resource/en/datasheet/bat48.pdf', 'kicadSymbolki_keywords': 'diode Schottky', 'kicadSymbolki_description': '40V 0.35A Small Signal Schottky Diode, SOD-323', 'kicadSymbolki_fp_filters': 'D*SOD?323*'}])
    newPart['name'].append('BAT48JFILM')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

