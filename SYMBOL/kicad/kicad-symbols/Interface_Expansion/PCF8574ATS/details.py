
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "PCF8574ATS"
    hexID = "SZKINTERFACEEXPANSIONPCF8574ATS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PCF8574TS', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCF8574ATS', 'kicadSymbolFootprint': 'Package_SO:SSOP-20_4.4x6.5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/PCF8574_PCF8574A.pdf', 'kicadSymbolki_keywords': 'I2C Expander', 'kicadSymbolki_description': '8 Bit Port/Expander to I2C Bus, SSOP-20', 'kicadSymbolki_fp_filters': 'SSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('Interface_Expansion : PCF8574ATS')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

