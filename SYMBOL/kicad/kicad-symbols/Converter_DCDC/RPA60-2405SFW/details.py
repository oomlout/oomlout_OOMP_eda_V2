
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Converter_DCDC"
    oIndex = "RPA60-2405SFW"
    hexID = "SZKCONRPA6245SFW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RPA60-2405SFW', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_RECOM_RPA60-xxxxSFW', 'kicadSymbolDatasheet': 'https://recom-power.com/pdf/Powerline_DC-DC/RPA60-FW.pdf', 'kicadSymbolki_keywords': 'isolated isolation dc-dc converter step-down', 'kicadSymbolki_description': 'Isolated 60W 4:1 input DC/DC converter module, 9-36V input voltage, 5V output voltage, DIP', 'kicadSymbolki_fp_filters': 'Converter*DCDC*RECOM*RPA60?xxxxSFW*'}])
    newPart['name'].append('RPA60-2405SFW')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

