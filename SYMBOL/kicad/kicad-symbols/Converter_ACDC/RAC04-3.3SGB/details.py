
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "RAC04-3.3SGB"
    hexID = "SZKCONRAC433SGB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RAC04-xxSGB', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'RAC04-3.3SGB', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_RECOM_RAC04-xxSGx_THT', 'kicadSymbolDatasheet': 'https://www.recom-power.com/pdf/Powerline-AC-DC/RAC04-GB.pdf', 'kicadSymbolki_keywords': 'ac dc power supply', 'kicadSymbolki_description': '4 Watt Single Output EMC Class B - 3.3V 1210mA', 'kicadSymbolki_fp_filters': 'Converter*ACDC*RECOM*RAC04*SG*'}])
    newPart['name'].append('RAC04-3.3SGB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

