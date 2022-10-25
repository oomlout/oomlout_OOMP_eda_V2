
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TCR2EE13"
    hexID = "SZKREGULATORLINEARTCR2EE13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TCR2EE11', 'kicadSymbolReference': 'U6', 'kicadSymbolValue': 'TCR2EE13', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-553', 'kicadSymbolDatasheet': 'https://toshiba.semicon-storage.com/info/docget.jsp?did=13794&prodName=TCR2EF45', 'kicadSymbolki_keywords': 'TOSHIBA LDO voltage regulator', 'kicadSymbolki_description': '200mA Low-dropout Voltage Regulator, Vout 1.3V, Vin up to 5.5V, SOT-553', 'kicadSymbolki_fp_filters': 'SOT?553*'}])
    newPart['name'].append('Regulator_Linear : TCR2EE13')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

