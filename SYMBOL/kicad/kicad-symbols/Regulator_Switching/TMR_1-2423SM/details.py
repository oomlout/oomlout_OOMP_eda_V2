
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TMR_1-2423SM"
    hexID = "SZKREGULATORSWITCHINGTMR12423SM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TMR_1-0522SM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMR_1-2423SM', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_TRACO_TMR-1SM_SMD', 'kicadSymbolDatasheet': 'http://assets.tracopower.com/TMR1SM/documents/tmr1sm-datasheet.pdf', 'kicadSymbolki_keywords': 'Murata isolated isolation dc-dc converter transformer', 'kicadSymbolki_description': '+/-33mA Regulated 1W DC/DC converter with 1.5kV isolation, 18V-36V input, +/-15V fixed Output Voltage, SMD', 'kicadSymbolki_fp_filters': 'Converter*DCDC*TRACO*TMR-1SM*SMD*'}])
    newPart['name'].append('Regulator_Switching : TMR_1-2423SM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

