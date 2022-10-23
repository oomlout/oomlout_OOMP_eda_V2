
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_AM_FM"
    oIndex = "LA1185"
    hexID = "SZKRFAMFMLA1185"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LA1185', 'kicadSymbolFootprint': 'Package_SIP:SIP-9_22.3x3mm_P2.54mm', 'kicadSymbolDatasheet': 'https://www.alldatasheet.com/datasheet-pdf/pdf/39974/SANYO/LA1185.html', 'kicadSymbolki_keywords': 'FM mixer receiver amplifier', 'kicadSymbolki_description': 'FM receiver front-end IC for radio-cassette recorder, music center applications, SIP-9', 'kicadSymbolki_fp_filters': 'SIP*22.3x3mm*P2.54mm*'}])
    newPart['name'].append('LA1185')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

