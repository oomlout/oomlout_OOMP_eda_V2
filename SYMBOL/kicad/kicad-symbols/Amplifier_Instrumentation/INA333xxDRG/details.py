
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Instrumentation"
    oIndex = "INA333xxDRG"
    hexID = "SZKAMPLIFIERINSTRUMENTATIONINA333XXDRG"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'INA333xxDRG', 'kicadSymbolFootprint': 'Package_SON:WSON-8-1EP_3x3mm_P0.5mm_EP1.45x2.4mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/ina333.pdf', 'kicadSymbolki_keywords': 'instrumentation opamp amplifier', 'kicadSymbolki_description': 'Zero Drift, Micropower Instrumentation Amplifier G = 1 + 100kOhm/Rg, WSON-8', 'kicadSymbolki_fp_filters': 'WSON*3x3mm*P0.5mm*'}])
    newPart['name'].append('INA333xxDRG')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

