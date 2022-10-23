
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_SMD"
    oIndex = "D_SMA-SMB_Universal_Handsoldering"
    hexID = "FZKDIODESMDSSMBUNIVERSALHANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_SMA-SMB_Universal_Handsoldering', 'description': 'Diode, Universal, SMA (DO-214AC) or SMB (DO-214AA), Handsoldering,', 'tags': 'Diode Universal SMA (DO-214AC) SMB (DO-214AA) Handsoldering ', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/D_SMB.wrl', 'pins': {'type': 'smd', 'shape': 'trapezoid'}})
    newPart['name'].append('Diode_SMD : D_SMA-SMB_Universal_Handsoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

