
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Simulation_SPICE"
    oIndex = "ISFFM"
    hexID = "SZKSIMULATIONSPICEISFFM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'I', 'kicadSymbolValue': 'ISFFM', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolSpice_Netlist_Enabled': 'Y', 'kicadSymbolSpice_Primitive': 'I', 'kicadSymbolSpice_Model': 'sffm(0 1 100k 5 1k)', 'kicadSymbolki_keywords': 'simulation frequency modulated', 'kicadSymbolki_description': 'Current source, single-frequency FM'}])
    newPart['name'].append('Simulation_SPICE : ISFFM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

