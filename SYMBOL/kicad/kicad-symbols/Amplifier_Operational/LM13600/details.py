
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LM13600"
    hexID = "SZKAMPLIFIEROPERATIONALLM136"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM13700', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM13600', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://pdf.datasheetcatalog.com/datasheet/nationalsemiconductor/DS007980.PDF', 'kicadSymbolki_keywords': 'operational transconductance amplifier OTA', 'kicadSymbolki_description': 'Dual Operational Transconductance Amplifiers with Linearizing Diodes and Buffers, DIP-16/SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9mm*P1.27mm* DIP*W7.62mm*'}])
    newPart['name'].append('LM13600')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

