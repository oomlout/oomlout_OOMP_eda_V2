
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Valve"
    oIndex = "Valve_Octal"
    hexID = "FZKVAVAOCTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Valve_Octal', 'description': '8-pin round valve', 'tags': 'valve', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Valve.3dshapes/Valve_Octal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Valve : Valve_Octal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

