
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-8-1EP_4x4mm_P0.8mm_EP1.98x3mm_ThermalVias"
    hexID = "FZKSONWSON81EP4X4P8EP198X3THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-8-1EP_4x4mm_P0.8mm_EP1.98x3mm_ThermalVias', 'description': 'WSON, 8 Pin (https://www.ti.com/lit/ds/symlink/lm5017.pdf#page=34), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WSON NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-8-1EP_4x4mm_P0.8mm_EP1.98x3mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SON : WSON-8-1EP_4x4mm_P0.8mm_EP1.98x3mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

