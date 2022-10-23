
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "R-781.8-1.0"
    hexID = "SZKREGULATORSWITCHINGR78181"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'R-78E5.0-0.5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'R-781.8-1.0', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_RECOM_R-78E-0.5_THT', 'kicadSymbolDatasheet': 'https://www.recom-power.com/pdf/Innoline/R-78xx-1.0.pdf', 'kicadSymbolki_keywords': 'dc-dc recom Step-Down DC/DC-Regulator', 'kicadSymbolki_description': '1A Step-Down DC/DC-Regulator, 4.75-18V input, 1.8V fixed Output Voltage, LM78xx replacement, -40°C to +85°C, SIP3', 'kicadSymbolki_fp_filters': 'Converter*DCDC*RECOM*R*78E*0.5*'}])
    newPart['name'].append('R-781.8-1.0')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

