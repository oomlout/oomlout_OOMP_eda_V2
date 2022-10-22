
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "RPM5.0-2.0"
    hexID = "SZKCONRPM52"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RPM5.0-6.0', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RPM5.0-2.0', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_RECOM_RPMx.x-x.0', 'kicadSymbolDatasheet': 'https://www.recom-power.com/pdf/Innoline/RPM-2.0.pdf', 'kicadSymbolki_keywords': 'Recom dc-dc converter', 'kicadSymbolki_description': '2A non-isolated switching regulator power module, 3-17V input voltage, 5.0V output voltage, DOSA', 'kicadSymbolki_fp_filters': 'Converter*DCDC*RECOM*RPM*'}])
    newPart['name'].append('RPM5.0-2.0')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

