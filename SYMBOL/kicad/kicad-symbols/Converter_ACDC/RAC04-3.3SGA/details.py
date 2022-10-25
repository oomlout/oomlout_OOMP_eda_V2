
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_ACDC"
    oIndex = "RAC04-3.3SGA"
    hexID = "SZKCONRAC433SGA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RAC04-xxSGA', 'kicadSymbolReference': 'PS', 'kicadSymbolValue': 'RAC04-3.3SGA', 'kicadSymbolFootprint': 'Converter_ACDC:Converter_ACDC_RECOM_RAC04-xxSGx_THT', 'kicadSymbolDatasheet': 'https://www.recom-power.com/pdf/Powerline-AC-DC/RAC04-GA.pdf', 'kicadSymbolki_keywords': 'ac dc power supply', 'kicadSymbolki_description': '4 Watt Single Output EMC Class A - 3.3V 1210mA', 'kicadSymbolki_fp_filters': 'Converter*ACDC*RECOM*RAC04*SG*'}])
    newPart['name'].append('Converter_ACDC : RAC04-3.3SGA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

