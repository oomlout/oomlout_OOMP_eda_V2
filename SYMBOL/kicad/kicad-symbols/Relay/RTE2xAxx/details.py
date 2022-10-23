
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "RTE2xAxx"
    hexID = "SZKRELAYRTE2XAXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RT42xAxx', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'RTE2xAxx', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_Schrack-RT2-FormC_RM5mm', 'kicadSymbolDatasheet': 'http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7FRT2_bistable%7F1116%7Fpdf%7FEnglish%7FENG_DS_RT2_bistable_1116.pdf%7F1-1415537-8', 'kicadSymbolki_keywords': 'TE DPDT CO bistable DC', 'kicadSymbolki_description': 'Schrack RT2 relay, bistable dual pole dual throw, single DC coil', 'kicadSymbolki_fp_filters': 'Relay*DPDT*RT2*FormC*'}])
    newPart['name'].append('RTE2xAxx')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

