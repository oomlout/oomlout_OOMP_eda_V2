
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Amplifier"
    oIndex = "SKY65404"
    hexID = "SZKRFAMPLIFIERSKY6544"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SKY65404', 'kicadSymbolFootprint': 'RF:Skyworks_SKY65404-31', 'kicadSymbolDatasheet': 'http://www.skyworksinc.com/uploads/documents/SKY65404_31_201512K.pdf', 'kicadSymbolki_keywords': 'LNA low noise amplifier RF', 'kicadSymbolki_description': '4.9-5.9GHz, 13dB Low-Noise Amplifier, QFN-6', 'kicadSymbolki_fp_filters': 'Skyworks*SKY65404*'}])
    newPart['name'].append('SKY65404')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

