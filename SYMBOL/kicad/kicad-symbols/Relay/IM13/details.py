
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "IM13"
    hexID = "SZKRELAYIM13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IM11', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'IM13', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=108-98001&DocType=SS&DocLang=EN', 'kicadSymbolki_keywords': 'relay monastable sensitive', 'kicadSymbolki_description': 'IM Relay, sensitive version, monostable, switching current 2/5A, power 60W/62.5VA, voltage 220VDC/250VAC', 'kicadSymbolki_fp_filters': 'Relay*DPDT*AXICOM*IMSeries*'}])
    newPart['name'].append('IM13')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

