
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "HS-40012"
    hexID = "SZKCONHS412"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HS-40003', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'HS-40012', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_Hahn_HS-400xx_THT', 'kicadSymbolDatasheet': 'http://www.tme.eu/de/Document/221b247820f4fbb72e0cbc1ee10acb85/HS40012.pdf', 'kicadSymbolki_keywords': '12V 3W AC-DC module power supply', 'kicadSymbolki_description': '12V, 3W, AC-DC module power supply, Hahn', 'kicadSymbolki_fp_filters': 'Converter*ACDC*Hahn*HS*400xx*'}])
    newPart['name'].append('HS-40012')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

