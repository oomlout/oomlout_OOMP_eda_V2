
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TMR_1-0523"
    hexID = "SZKREGULATORSWITCHINGTMR1523"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TMR_1-0522', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TMR_1-0523', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_TRACO_TMR-1-xxxx_Dual_THT', 'kicadSymbolDatasheet': 'http://assets.tracopower.com/TMR1/documents/tmr1-datasheet.pdf', 'kicadSymbolki_keywords': 'Murata isolated isolation dc-dc converter transformer', 'kicadSymbolki_description': '+/-33mA Regulated 1W DC/DC converter with 1.5kV isolation, 4.5V-9V input, +/-15V fixed Output Voltage, SIP-6', 'kicadSymbolki_fp_filters': 'Converter*DCDC*TRACO*TMR?1*Dual*'}])
    newPart['name'].append('Regulator_Switching : TMR_1-0523')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

