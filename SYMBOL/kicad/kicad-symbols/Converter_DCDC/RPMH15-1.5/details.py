
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "RPMH15-1.5"
    hexID = "SZKCONRPMH1515"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RPMH3.3-1.5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RPMH15-1.5', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_RECOM_RPMx.x-x.0', 'kicadSymbolDatasheet': 'https://recom-power.com/pdf/Innoline/RPMH-1.5.pdf', 'kicadSymbolki_keywords': 'Recom DC-DC converter', 'kicadSymbolki_description': '1.5A non-isolated switching regulator power module, 17-60V input voltage, 15V output voltage', 'kicadSymbolki_fp_filters': 'Converter*DCDC*RECOM*RPM*'}])
    newPart['name'].append('Converter_DCDC : RPMH15-1.5')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

