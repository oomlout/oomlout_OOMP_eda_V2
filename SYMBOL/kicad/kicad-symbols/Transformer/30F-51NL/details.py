
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "30F-51NL"
    hexID = "SZKTR3F51NL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TR', 'kicadSymbolValue': '30F-51NL', 'kicadSymbolFootprint': 'Transformer_SMD:Transformer_Ethernet_YDS_30F-51NL_SO-24_7.1x15.1mm', 'kicadSymbolDatasheet': 'https://datasheet.lcsc.com/lcsc/1811051610_Shanghai-YDS-Tech-30F-51NL_C123168.pdf', 'kicadSymbolki_keywords': 'gigabit RJ45 transformer ethernet lan', 'kicadSymbolki_description': '1CT:1CT 10/100/1000 Base-T Ethernet Transformer, SMD-24', 'kicadSymbolki_fp_filters': 'Transformer*Ethernet*YDS*30F?51NL*'}])
    newPart['name'].append('30F-51NL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

