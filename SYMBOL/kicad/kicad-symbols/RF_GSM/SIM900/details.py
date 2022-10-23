
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GSM"
    oIndex = "SIM900"
    hexID = "SZKGSMSIM9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SIM900', 'kicadSymbolFootprint': 'RF_GSM:SIMCom_SIM900', 'kicadSymbolDatasheet': 'http://simcom.ee/documents/SIM900/SIM900_Hardware%20Design_V2.05.pdf', 'kicadSymbolki_keywords': 'GSM GPRS Quad-Band SMS FAX', 'kicadSymbolki_description': 'GSM Quad-Band Communication Module, GPRS, Audio Engine, AT Command Set', 'kicadSymbolki_fp_filters': 'SIMCom*SIM900*'}])
    newPart['name'].append('SIM900')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

