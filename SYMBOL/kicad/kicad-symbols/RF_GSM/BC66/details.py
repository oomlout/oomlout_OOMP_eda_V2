
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GSM"
    oIndex = "BC66"
    hexID = "SZKGSMBC66"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BC66', 'kicadSymbolFootprint': 'RF_GSM:Quectel_BC66', 'kicadSymbolDatasheet': 'https://www.quectel.com/UploadImage/Downlad/Quectel_BC66_Hardware_Design_V1.1.pdf', 'kicadSymbolki_keywords': 'NB-IoT Data SMS', 'kicadSymbolki_description': 'Quectel NB-IoT Global, AT Command Set', 'kicadSymbolki_fp_filters': 'Quectel*BC66*'}])
    newPart['name'].append('BC66')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

