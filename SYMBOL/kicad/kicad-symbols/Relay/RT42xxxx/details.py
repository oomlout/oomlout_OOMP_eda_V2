
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "RT42xxxx"
    hexID = "SZKRELAYRT42XXXX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'RT42xxxx', 'kicadSymbolFootprint': 'Relay_THT:Relay_DPDT_Schrack-RT2-FormC_RM5mm', 'kicadSymbolDatasheet': 'http://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7FRT2%7F1014%7Fpdf%7FEnglish%7FENG_DS_RT2_1014.pdf%7F6-1393243-3', 'kicadSymbolki_keywords': 'TE DPDT CO monostable', 'kicadSymbolki_description': 'Schrack RT2 relay, monostable dual pole dual throw, DC or AC coil', 'kicadSymbolki_fp_filters': 'Relay*DPDT*RT2*FormC*'}])
    newPart['name'].append('Relay : RT42xxxx')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

