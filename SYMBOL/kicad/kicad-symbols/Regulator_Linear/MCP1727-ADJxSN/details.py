
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MCP1727-ADJxSN"
    hexID = "SZKREGULATORLINEARMCP1727ADJXSN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP1727-ADJxSN', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/aemtest/APID/ProductDocuments/DataSheets/MCP1727-1.5A-Low-Voltage-Low-Quiescent-Current-LDO-Regulator-20001999D.pdf', 'kicadSymbolki_keywords': 'Low Voltage Low Quiescent Current Adjustable LDO Regulator', 'kicadSymbolki_description': '1.5A, Low Voltage, Low Quiescent Current LDO Regulator, 2.3 - 6V Input, Adjustable Output, 330mV Dropout, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('MCP1727-ADJxSN')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

