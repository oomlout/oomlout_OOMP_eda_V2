
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Simulation_SPICE"
    oIndex = "VDC"
    hexID = "SZKSIMULATIONSPICEVDC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'V', 'kicadSymbolValue': 'VDC', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolSpice_Netlist_Enabled': 'Y', 'kicadSymbolSpice_Primitive': 'V', 'kicadSymbolSpice_Model': 'dc(1)', 'kicadSymbolki_keywords': 'simulation', 'kicadSymbolki_description': 'Voltage source, DC'}])
    newPart['name'].append('Simulation_SPICE : VDC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

