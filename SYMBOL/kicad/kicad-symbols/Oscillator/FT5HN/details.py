
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "FT5HN"
    hexID = "SZKOCSFT5HN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FT5HN', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_Fox_FT5H_5.0x3.2mm', 'kicadSymbolDatasheet': 'https://foxonline.com/wp-content/uploads/pdfs/T5HN_T5HV.pdf', 'kicadSymbolki_keywords': 'TXCO', 'kicadSymbolki_description': 'HCMOS temperature compensated oscillator', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*Fox*FT5H*5.0x3.2mm*'}])
    newPart['name'].append('FT5HN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

