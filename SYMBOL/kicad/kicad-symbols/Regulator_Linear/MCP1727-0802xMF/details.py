
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MCP1727-0802xMF"
    hexID = "SZKREGULATORLINEARMCP172782XMF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MCP1727-0802xMF', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_3x3mm_P0.65mm_EP1.55x2.4mm', 'kicadSymbolDatasheet': 'https://ww1.microchip.com/downloads/aemtest/APID/ProductDocuments/DataSheets/MCP1727-1.5A-Low-Voltage-Low-Quiescent-Current-LDO-Regulator-20001999D.pdf', 'kicadSymbolki_keywords': 'Low Voltage Low Quiescent Current Fixed LDO Regulator', 'kicadSymbolki_description': '1.5A, Low Voltage, Low Quiescent Current LDO Regulator, 2.3 - 6V Input, Fixed 0.8V Output, 330mV Dropout, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*3x3mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Linear : MCP1727-0802xMF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

