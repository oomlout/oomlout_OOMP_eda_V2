
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Simulation_SPICE"
    oIndex = "IAM"
    hexID = "SZKSIMULATIONSPICEIAM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'I', 'kicadSymbolValue': 'IAM', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolSpice_Netlist_Enabled': 'Y', 'kicadSymbolSpice_Primitive': 'I', 'kicadSymbolSpice_Model': 'am(1 0 100k 1k 1n)', 'kicadSymbolki_keywords': 'simulation amplitude modulated', 'kicadSymbolki_description': 'Current source, AM'}])
    newPart['name'].append('Simulation_SPICE : IAM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

