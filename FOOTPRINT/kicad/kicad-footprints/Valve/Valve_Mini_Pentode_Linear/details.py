
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Valve"
    oIndex = "Valve_Mini_Pentode_Linear"
    hexID = "FZKVAVAMPENTODELINEAR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Valve_Mini_Pentode_Linear', 'description': 'Mini-Pentode, 5-pin, e.g. JAN6418', 'tags': 'Valve Mini-Pentode 5-pin JAN6418', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Valve.3dshapes/Valve_Mini_Pentode_Linear.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Valve : Valve_Mini_Pentode_Linear')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

