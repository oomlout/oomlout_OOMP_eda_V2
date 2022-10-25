
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "PCF8574A"
    hexID = "SZKINTERFACEEXPANSIONPCF8574A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PCF8574', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCF8574A', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/PCF8574_PCF8574A.pdf', 'kicadSymbolki_keywords': 'I2C Expander', 'kicadSymbolki_description': '8 Bit Port/Expander to I2C Bus, DIP/SOIC-16', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SOIC*7.5x10.3mm*P1.27mm*'}])
    newPart['name'].append('Interface_Expansion : PCF8574A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

