
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "R-78C9.0-1.0"
    hexID = "SZKREGULATORSWITCHINGR78C91"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'R-78E5.0-0.5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'R-78C9.0-1.0', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_RECOM_R-78E-0.5_THT', 'kicadSymbolDatasheet': 'https://www.recom-power.com/pdf/Innoline/R-78Cxx-1.0.pdf', 'kicadSymbolki_keywords': 'dc-dc recom Step-Down DC/DC-Regulator', 'kicadSymbolki_description': '1A Step-Down DC/DC-Regulator, 12-42V input, 9V fixed Output Voltage, LM78xx replacement, -40°C to +85°C, SIP3', 'kicadSymbolki_fp_filters': 'Converter*DCDC*RECOM*R*78E*0.5*'}])
    newPart['name'].append('Regulator_Switching : R-78C9.0-1.0')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

