
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TSR_1-2465"
    hexID = "SZKREGULATORSWITCHINGTSR12465"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TSR_1-2450', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TSR_1-2465', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_TRACO_TSR-1_THT', 'kicadSymbolDatasheet': 'http://www.tracopower.com/products/tsr1.pdf', 'kicadSymbolki_keywords': 'dc-dc traco buck', 'kicadSymbolki_description': '1A step-down regulator module, fixed 6.5V output voltage, 9-36V input voltage, -40°C to +85°C temperature range, TO-220 compatible LM78xx replacement', 'kicadSymbolki_fp_filters': 'Converter*DCDC*TRACO*TSR?1*'}])
    newPart['name'].append('Regulator_Switching : TSR_1-2465')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

