
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm_ThermalVias"
    hexID = "FZKSONWSON61EP2X2P65EP1X16THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm_ThermalVias', 'description': 'WSON, 6 Pin (http://www.ti.com/lit/ds/symlink/tps61040.pdf#page=35), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'WSON NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SON : WSON-6-1EP_2x2mm_P0.65mm_EP1x1.6mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

