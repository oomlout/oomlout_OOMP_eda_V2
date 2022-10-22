
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "TMR2-4812WI"
    hexID = "SZKCONTMR24812WI"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TMR2-2410WI', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMR2-4812WI', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_TRACO_TMR-2xxxxWI_THT', 'kicadSymbolDatasheet': 'https://www.tracopower.com/products/tmr2wi.pdf', 'kicadSymbolki_keywords': 'Traco isolated isolation dc-dc converter transformer', 'kicadSymbolki_description': '165mA Regulated 2W DC/DC converter with 1.5kV isolation, 18V-75V input, 12V fixed Output Voltage, SIP-9', 'kicadSymbolki_fp_filters': 'Converter*DCDC*TRACO*TMR*2xxxxWI*'}])
    newPart['name'].append('TMR2-4812WI')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

