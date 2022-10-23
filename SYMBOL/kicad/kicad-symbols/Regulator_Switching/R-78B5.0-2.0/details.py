
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "R-78B5.0-2.0"
    hexID = "SZKREGULATORSWITCHINGR78B52"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'R-78B1.2-2.0', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'R-78B5.0-2.0', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_RECOM_R-78B-2.0_THT', 'kicadSymbolDatasheet': 'https://www.recom-power.com/pdf/Innoline/R-78Bxx-2.0.pdf', 'kicadSymbolki_keywords': 'dc-dc recom Step-Down DC/DC-Regulator', 'kicadSymbolki_description': '2A Step-Down DC/DC-Regulator, 6.5-32V input, 5.0V fixed Output Voltage, LM78xx replacement, -40°C to +85°C, SIP3', 'kicadSymbolki_fp_filters': 'Converter*DCDC*RECOM*R*78B*2.0*'}])
    newPart['name'].append('R-78B5.0-2.0')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

