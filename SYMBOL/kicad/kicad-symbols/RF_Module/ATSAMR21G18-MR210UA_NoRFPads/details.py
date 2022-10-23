
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Module"
    oIndex = "ATSAMR21G18-MR210UA_NoRFPads"
    hexID = "SZKRFMOATSAMR21G18MR21UANORFPADS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ATSAMR21G18-MR210UA_NoRFPads', 'kicadSymbolFootprint': 'RF_Module:Atmel_ATSAMR21G18-MR210UA_NoRFPads', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/devicedoc/atmel-42475-atsamr21g18-mr210ua_datasheet.pdf', 'kicadSymbolki_keywords': 'Wireless Zigbee 802.15.4 ATSAMR21G18 AT45DB041E TECC508A', 'kicadSymbolki_description': 'RF Module, ATSAMR21, Zigbee 802.15.4, external antenna, SMD', 'kicadSymbolki_fp_filters': 'Atmel*ATSAMR21G18*MR210UA*NoRFPads*'}])
    newPart['name'].append('ATSAMR21G18-MR210UA_NoRFPads')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

