
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "RPA60-2424SFW"
    hexID = "SZKCONRPA62424SFW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'RPA60-2405SFW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RPA60-2424SFW', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_RECOM_RPA60-xxxxSFW', 'kicadSymbolDatasheet': 'https://recom-power.com/pdf/Powerline_DC-DC/RPA60-FW.pdf', 'kicadSymbolki_keywords': 'isolated isolation dc-dc converter step-down', 'kicadSymbolki_description': 'Isolated 60W 4:1 input DC/DC converter module, 9-36V input voltage, 24V output voltage, DIP', 'kicadSymbolki_fp_filters': 'Converter*DCDC*RECOM*RPA60?xxxxSFW*'}])
    newPart['name'].append('Converter_DCDC : RPA60-2424SFW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

