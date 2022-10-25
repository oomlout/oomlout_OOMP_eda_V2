
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "NMA1512DC"
    hexID = "SZKREGULATORSWITCHINGNMA1512DC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'NMA0512DC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NMA1512DC', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Murata_NMAxxxxDC_THT', 'kicadSymbolDatasheet': 'http://power.murata.com/data/power/ncl/kdc_nma.pdf', 'kicadSymbolki_keywords': 'Murata isolated isolation dc-dc converter', 'kicadSymbolki_description': '+/-42mA Isolated 1W Dual output DC/DC Converter Module, 15V Input Voltage, +/-12V Output Voltage, DIP Package', 'kicadSymbolki_fp_filters': 'Converter*DCDC*Murata*NMAxxxxDC*'}])
    newPart['name'].append('Regulator_Switching : NMA1512DC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

