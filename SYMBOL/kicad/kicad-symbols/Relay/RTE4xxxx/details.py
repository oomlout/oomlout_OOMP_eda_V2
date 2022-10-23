
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "RTE4xxxx"
    hexID = "SZKRELAYRTE4XXXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RT44xxxx', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'RTE4xxxx', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPST_Schrack-RT2-FormA_RM5mm', 'kicadSymbolDatasheet': 'http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7FRT2%7F1014%7Fpdf%7FEnglish%7FENG_DS_RT2_1014.pdf%7F6-1393243-3', 'kicadSymbolki_keywords': 'TE DPST NO monostable', 'kicadSymbolki_description': 'Schrack RT2 relay, monostable dual pole normally open, DC or AC coil', 'kicadSymbolki_fp_filters': 'Relay*DPST*RT2*FormA*'}])
    newPart['name'].append('RTE4xxxx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

