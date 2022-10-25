
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "IM40"
    hexID = "SZKRELAYIM4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'IM40', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=108-98001&DocType=SS&DocLang=EN', 'kicadSymbolki_keywords': 'relay bistable', 'kicadSymbolki_description': 'IM Relay, standard version, bistable, switching current 2/5A, power 60W/62.5VA, voltage 220VDC/250VAC', 'kicadSymbolki_fp_filters': 'Relay*DPDT*AXICOM*IMSeries*'}])
    newPart['name'].append('Relay : IM40')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

