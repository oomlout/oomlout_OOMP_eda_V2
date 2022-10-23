
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transformer"
    oIndex = "LL1587"
    hexID = "SZKTRLL1587"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'T', 'kicadSymbolValue': 'LL1587', 'kicadSymbolFootprint': 'Transformer_THT:Transformer_Microphone_Lundahl_LL1587', 'kicadSymbolDatasheet': 'http://www.lundahl.se/wp-content/uploads/datasheets/1587.pdf', 'kicadSymbolki_keywords': 'microphone transformer', 'kicadSymbolki_description': 'Lundahl Transformers, Microphone Transformer', 'kicadSymbolki_fp_filters': 'Transformer*Microphone*Lundahl*LL1587*'}])
    newPart['name'].append('LL1587')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

