
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "RPM5.0-6.0"
    hexID = "SZKCONRPM56"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RPM5.0-6.0', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_RECOM_RPMx.x-x.0', 'kicadSymbolDatasheet': 'https://www.recom-power.com/pdf/Innoline/RPM-6.0.pdf', 'kicadSymbolki_keywords': 'Recom dc-dc converter', 'kicadSymbolki_description': '6A non-isolated switching regulator power module, 4-15V input voltage, 5.0V output voltage, DOSA', 'kicadSymbolki_fp_filters': 'Converter*DCDC*RECOM*RPM*'}])
    newPart['name'].append('Converter_DCDC : RPM5.0-6.0')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

