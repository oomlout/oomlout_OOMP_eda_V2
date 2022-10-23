
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_AM_FM"
    oIndex = "Si4734-D60-GU"
    hexID = "SZKRFAMFMSI4734D6GU"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Si4735-D60-GU', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si4734-D60-GU', 'kicadSymbolFootprint': 'Package_SO:SSOP-24_3.9x8.7mm_P0.635mm', 'kicadSymbolDatasheet': 'http://www.silabs.com/Support%20Documents/TechnicalDocs/Si4730-31-34-35-D60.pdf', 'kicadSymbolki_keywords': 'Broadcast AM FM SW LW Radio Receiver', 'kicadSymbolki_description': 'AM/FM/SW/LW Broadcast Radio Receiver', 'kicadSymbolki_fp_filters': 'SSOP*3.9x8.7mm*P0.635mm*'}])
    newPart['name'].append('Si4734-D60-GU')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

