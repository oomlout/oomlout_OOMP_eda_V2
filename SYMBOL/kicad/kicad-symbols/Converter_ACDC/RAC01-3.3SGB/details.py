
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "RAC01-3.3SGB"
    hexID = "SZKCONRAC133SGB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RAC01-xxSGB', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'RAC01-3.3SGB', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_RECOM_RAC01-xxSGB_THT', 'kicadSymbolDatasheet': 'https://www.recom-power.com/pdf/Powerline-AC-DC/RAC01-GB.pdf', 'kicadSymbolki_keywords': 'ac dc power supply', 'kicadSymbolki_description': '1 Watt Single Output EMC Class B AC/DC 3.3V 303mA power supply with regulated and short-circuit-proof isolated DC outputs and low standby power consumption.', 'kicadSymbolki_fp_filters': 'Converter*ACDC*RECOM*RAC01*SGB*THT*'}])
    newPart['name'].append('RAC01-3.3SGB')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

