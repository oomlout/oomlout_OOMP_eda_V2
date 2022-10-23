
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GSM"
    oIndex = "SIM7020E"
    hexID = "SZKGSMSIM72E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SIM7020E', 'kicadSymbolFootprint': 'RF_GSM:SIMCom_SIM800C', 'kicadSymbolDatasheet': 'https://simcom.ee/documents/SIM7020/SIM7020%20Hardware%20Design_V1.02.pdf', 'kicadSymbolki_keywords': 'NB-IoT Data SMS', 'kicadSymbolki_description': 'NB-IoT B1/B3/B5/B8/B20/B28, AT Command Set', 'kicadSymbolki_fp_filters': 'SIMCom*SIM800C*'}])
    newPart['name'].append('SIM7020E')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

