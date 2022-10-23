
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "DMC3071LVT"
    hexID = "SZKTRANSISTORFETDMC371LVT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DMC2053UVT', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'DMC3071LVT', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TSOT-23-6', 'kicadSymbolDatasheet': 'https://www.diodes.com/assets/Datasheets/DMC3071LVT.pdf', 'kicadSymbolki_keywords': 'complementary mosfet', 'kicadSymbolki_description': '3.4A/-2.7A Id, 30V Vds, Complementary pair enhancement mode P-Channel and N-Channel MOSFET, TSOT-23-6', 'kicadSymbolki_fp_filters': 'TSOT?23*'}])
    newPart['name'].append('DMC3071LVT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

