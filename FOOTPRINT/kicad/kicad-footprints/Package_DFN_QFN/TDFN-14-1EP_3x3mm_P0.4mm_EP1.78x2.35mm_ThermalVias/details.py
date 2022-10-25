
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "TDFN-14-1EP_3x3mm_P0.4mm_EP1.78x2.35mm_ThermalVias"
    hexID = "FZKDFNTDFN141EP3X3P4EP178X235THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TDFN-14-1EP_3x3mm_P0.4mm_EP1.78x2.35mm_ThermalVias', 'description': 'TDFN, 14 Pin (https://pdfserv.maximintegrated.com/package_dwgs/21-0137.PDF (T1433-2C)), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'TDFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TDFN-14-1EP_3x3mm_P0.4mm_EP1.78x2.35mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : TDFN-14-1EP_3x3mm_P0.4mm_EP1.78x2.35mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

