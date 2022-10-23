
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "R-78S3.3-0.1"
    hexID = "SZKREGULATORSWITCHINGR78S331"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'R-78S3.3-0.1', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_RECOM_R-78S-0.1_THT', 'kicadSymbolDatasheet': 'https://www.recom-power.com/pdf/Innoline/R-78Sxx-0.1.pdf', 'kicadSymbolki_keywords': 'dc-dc recom Step-Down DC/DC-Regulator', 'kicadSymbolki_description': '100mA Step-Up DC/DC-Regulator, 0.65-3.15V input, 3.3V fixed Output Voltage, LM78xx replacement, -40°C to +85°C, SIP4', 'kicadSymbolki_fp_filters': 'Converter*DCDC*RECOM*R*78S*0.1*'}])
    newPart['name'].append('R-78S3.3-0.1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

