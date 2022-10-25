
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "R-78HB24-0.3"
    hexID = "SZKREGULATORSWITCHINGR78HB243"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'R-78HB24-0.3', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_RECOM_R-78HB-0.5_THT', 'kicadSymbolDatasheet': 'https://www.recom-power.com/pdf/Innoline/R-78HBxx-0.5_L.pdf', 'kicadSymbolki_keywords': 'dc-dc recom Step-Down DC/DC-Regulator', 'kicadSymbolki_description': '300mA Step-Down DC/DC-Regulator, 36-72V input, 24V fixed Output Voltage, LM78xx replacement, -40°C to +85°C, SIP3', 'kicadSymbolki_fp_filters': 'Converter*DCDC*RECOM*R*78HB*0.5*'}])
    newPart['name'].append('Regulator_Switching : R-78HB24-0.3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

