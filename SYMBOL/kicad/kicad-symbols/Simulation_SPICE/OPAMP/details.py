
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Simulation_SPICE"
    oIndex = "OPAMP"
    hexID = "SZKSIMULATIONSPICEOPAMP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'OPAMP', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolSpice_Netlist_Enabled': 'Y', 'kicadSymbolSpice_Primitive': 'X', 'kicadSymbolki_keywords': 'simulation', 'kicadSymbolki_description': 'Operational amplifier, single, node sequence=1:+ 2:- 3:OUT 4:V+ 5:V-'}])
    newPart['name'].append('Simulation_SPICE : OPAMP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

