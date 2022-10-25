
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_SMD"
    oIndex = "D_SMB_Modified"
    hexID = "FZKDIODESMDSMBMODIFIED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'D_SMB_Modified', 'description': 'Diode SMB (DO-214AA) Modified (http://www.littelfuse.com/~/media/electronics/datasheets/sidactors/littelfuse_sidactor_battrax_positive_negative_modified_do_214_datasheet.pdf.pdf)', 'tags': 'Diode SMB (DO-214AA)', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_SMD.3dshapes/D_SMB_Modified.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Diode_SMD : D_SMB_Modified')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

