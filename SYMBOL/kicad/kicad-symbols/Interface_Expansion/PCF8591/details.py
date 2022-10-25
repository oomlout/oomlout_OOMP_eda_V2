
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "PCF8591"
    hexID = "SZKINTERFACEEXPANSIONPCF8591"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCF8591', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/PCF8591.pdf', 'kicadSymbolki_keywords': 'I2C ADC DAC', 'kicadSymbolki_description': '4ch ADC, 1 DAC, I2C Bus Interface, DIP/SOIC-16', 'kicadSymbolki_fp_filters': 'DIP* PDIP* SO* SOIC*'}])
    newPart['name'].append('Interface_Expansion : PCF8591')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

