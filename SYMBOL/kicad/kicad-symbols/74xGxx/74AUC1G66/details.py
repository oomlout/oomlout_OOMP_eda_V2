
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xGxx"
    oIndex = "74AUC1G66"
    hexID = "SZK74XGXX74AUC1G66"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LVC1G66', 'kicadSymbolReference': 'U', 'kicadSymbolValue': '74AUC1G66', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/sn74auc1g66.pdf', 'kicadSymbolki_keywords': 'Single Bilateral Analog Switch', 'kicadSymbolki_description': 'Single Bilateral Analog Switch, SOT-23-5/SC-70-5', 'kicadSymbolki_fp_filters': 'SOT* SC*'}])
    newPart['name'].append('74AUC1G66')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

