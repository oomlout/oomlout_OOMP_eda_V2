
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "TSL2550T"
    hexID = "SZKSENOPTICALTSL255T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSL2550T', 'kicadSymbolFootprint': 'OptoDevice:AMS_TSL2550_SMD', 'kicadSymbolDatasheet': 'http://ams.com/eng/content/download/250130/975613/142977', 'kicadSymbolki_keywords': 'opto ambient light sensor', 'kicadSymbolki_description': 'Ambient Light Sensor with SMbus Interface, T-4 interface SMD', 'kicadSymbolki_fp_filters': 'AMS*TSL2550*SMD*'}])
    newPart['name'].append('TSL2550T')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

