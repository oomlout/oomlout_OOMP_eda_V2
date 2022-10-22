
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "1N62xxCA"
    hexID = "SZKDIODE1N62XXCA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1.5KExxCA', 'kicadSymbolReference': 'D', 'kicadSymbolValue': '1N62xxCA', 'kicadSymbolFootprint': 'Diode_THT:D_DO-201AE_P15.24mm_Horizontal', 'kicadSymbolDatasheet': 'https://www.vishay.com/docs/88301/15ke.pdf', 'kicadSymbolki_keywords': 'diode TVS voltage suppressor', 'kicadSymbolki_description': '1500W bidirectional TRANSZORB® Transient Voltage Suppressor, DO-201AE', 'kicadSymbolki_fp_filters': 'D?DO?201AE*'}])
    newPart['name'].append('1N62xxCA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

