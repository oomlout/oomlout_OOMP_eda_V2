
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "RT42xFxx"
    hexID = "SZKRELAYRT42XFXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'RT42xFxx', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_Schrack-RT2-FormC-Dual-Coil_RM5mm', 'kicadSymbolDatasheet': 'http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7FRT2_bistable%7F1116%7Fpdf%7FEnglish%7FENG_DS_RT2_bistable_1116.pdf%7F1-1415537-8', 'kicadSymbolki_keywords': 'TE DPDT CO bistable DC', 'kicadSymbolki_description': 'Schrack RT2 relay, bistable dual pole dual throw, dual DC coils', 'kicadSymbolki_fp_filters': 'Relay*DPDT*RT2*FormC*'}])
    newPart['name'].append('RT42xFxx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

