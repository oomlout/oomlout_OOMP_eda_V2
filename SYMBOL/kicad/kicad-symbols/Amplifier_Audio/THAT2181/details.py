
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "THAT2181"
    hexID = "SZKAMPLIFIERAUDIOTHAT2181"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'THAT2181', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.thatcorp.com/datashts/THAT_2181-Series_Datasheet.pdf', 'kicadSymbolki_keywords': 'audio vca', 'kicadSymbolki_description': 'Blackmer Trimmable IC Voltage Controlled Amplifiers, SIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'SIP*19x3mm*P2.54mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('THAT2181')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

