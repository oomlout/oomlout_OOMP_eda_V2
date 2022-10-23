
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM22678TJ-ADJ"
    hexID = "SZKREGULATORSWITCHINGLM22678TJADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM22678TJ-ADJ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-7_TabPin8', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/lm22678.pdf', 'kicadSymbolki_keywords': 'DC/DC Buck Converter 5A', 'kicadSymbolki_description': '5A Step-Down Switching Voltage Regulater, 4.5-42V Input, Adjustable Output, 500kHz Switching Frequency, TO-263', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('LM22678TJ-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

