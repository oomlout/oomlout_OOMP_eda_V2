
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SON"
    oIndex = "VSON-10-1EP_3x3mm_P0.5mm_EP1.2x2mm_ThermalVias"
    hexID = "FZKSONVSON11EP3X3P5EP12X2THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'VSON-10-1EP_3x3mm_P0.5mm_EP1.2x2mm_ThermalVias', 'description': 'VSON, 10 Pin (http://rohmfs.rohm.com/en/products/databook/datasheet/ic/power/switching_regulator/bd8314nuv-e.pdf (Page 20)), generated with kicad-footprint-generator ipc_noLead_generator.py', 'tags': 'VSON NoLead', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/VSON-10-1EP_3x3mm_P0.5mm_EP1.2x2mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SON : VSON-10-1EP_3x3mm_P0.5mm_EP1.2x2mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

