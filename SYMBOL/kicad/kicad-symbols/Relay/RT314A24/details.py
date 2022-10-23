
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "RT314A24"
    hexID = "SZKRELAYRT314A24"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RT314A03', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'RT314A24', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPDT_Schrack-RT1-16A-FormC_RM5mm', 'kicadSymbolDatasheet': 'https://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=RT1_bistable&DocType=DS&DocLang=English', 'kicadSymbolki_keywords': 'TE SPDT 1P2T CO bistable DC', 'kicadSymbolki_description': 'Schrack RT1 relay, bistable single pole dual throw, single DC coil, 24V, IEC 60335-1', 'kicadSymbolki_fp_filters': 'Relay*SPDT*Schrack*RT1*16A*FormC*RM5mm*'}])
    newPart['name'].append('RT314A24')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

