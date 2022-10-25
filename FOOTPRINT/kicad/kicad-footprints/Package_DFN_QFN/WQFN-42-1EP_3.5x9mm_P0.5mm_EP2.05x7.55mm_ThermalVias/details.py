
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_DFN_QFN"
    oIndex = "WQFN-42-1EP_3.5x9mm_P0.5mm_EP2.05x7.55mm_ThermalVias"
    hexID = "FZKDFNWQFN421EP35X9P5EP25X755THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WQFN-42-1EP_3.5x9mm_P0.5mm_EP2.05x7.55mm_ThermalVias', 'description': 'WQFN, 42 Pin (http://www.ti.com/lit/ds/symlink/ts3l501e.pdf#page=23), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WQFN NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WQFN-42-1EP_3.5x9mm_P0.5mm_EP2.05x7.55mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_DFN_QFN : WQFN-42-1EP_3.5x9mm_P0.5mm_EP2.05x7.55mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

