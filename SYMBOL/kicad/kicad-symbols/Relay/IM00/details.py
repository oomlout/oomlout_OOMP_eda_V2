
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "IM00"
    hexID = "SZKRELAYIM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'IM00', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.te.com/commerce/DocumentDelivery/DDEController?Action=srchrtrv&DocNm=108-98001&DocType=SS&DocLang=EN', 'kicadSymbolki_keywords': 'relay monostable', 'kicadSymbolki_description': 'IM Relay, standard version, monostable, switching current 2/5A, power 60W/62.5VA, voltage 220VDC/250VAC, THT package', 'kicadSymbolki_fp_filters': 'Relay*DPDT*AXICOM*IMSeries*'}])
    newPart['name'].append('Relay : IM00')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

