
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "TMR-2412"
    hexID = "SZKCONTMR2412"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TMR-0510', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMR-2412', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_TRACO_TMR-xxxx_THT', 'kicadSymbolDatasheet': 'https://www.tracopower.com/products/tmr2.pdf', 'kicadSymbolki_keywords': 'Traco isolated isolation dc-dc converter transformer', 'kicadSymbolki_description': '165mA Regulated 2W DC/DC converter with 1.5kV isolation, 18V-36V input, 12V fixed Output Voltage, SIP-8', 'kicadSymbolki_fp_filters': 'Converter*DCDC*TRACO*TMR*xxxx*'}])
    newPart['name'].append('TMR-2412')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

