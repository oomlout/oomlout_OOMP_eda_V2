
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_SMD"
    oIndex = "D_SMB-SMC_Universal_Handsoldering"
    hexID = "FZKDIODESMDSMBSMCUNIVERSALHANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_SMB-SMC_Universal_Handsoldering', 'description': 'Diode, Universal, SMB(DO-214AA) or SMC (DO-214AB), Handsoldering,', 'tags': 'Diode Universal SMB(DO-214AA) SMC (DO-214AB) Handsoldering ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/D_SMC.wrl', 'pins': {'type': 'smd', 'shape': 'trapezoid'}})
    newPart['name'].append('Diode_SMD : D_SMB-SMC_Universal_Handsoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

