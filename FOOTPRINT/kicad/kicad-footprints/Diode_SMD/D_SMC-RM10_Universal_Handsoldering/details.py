
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_SMD"
    oIndex = "D_SMC-RM10_Universal_Handsoldering"
    hexID = "FZKDIODESMDSMCRM1UNIVERSALHANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_SMC-RM10_Universal_Handsoldering', 'description': 'Diode, Universal, SMC (DO-214AB), RM10, Handsoldering, SMD, Thruhole', 'tags': 'Diode Universal SMC (DO-214AB) RM10 Handsoldering SMD Thruhole', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/D_SMC.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_SMD : D_SMC-RM10_Universal_Handsoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

