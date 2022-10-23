
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_ZigBee"
    oIndex = "XBee_SMT"
    hexID = "SZKRFZIGBEEXBEES"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'XBee_SMT', 'kicadSymbolFootprint': 'RF_Module:Digi_XBee_SMT', 'kicadSymbolDatasheet': 'http://www.digi.com/resources/documentation/digidocs/pdfs/90002126.pdf', 'kicadSymbolki_keywords': 'Digi XBee', 'kicadSymbolki_description': 'Digi Xbee SMT RF module', 'kicadSymbolki_fp_filters': 'Digi*XBee*SMT*'}])
    newPart['name'].append('XBee_SMT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

