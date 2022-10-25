
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_FFC-FPC"
    oIndex = "Omron_XF2M-4015-1A_1x40-1MP_P0.5mm_Horizontal"
    hexID = "FZKCNFFCFPCOMRONXF2M4151A1X41MPP5HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Omron_XF2M-4015-1A_1x40-1MP_P0.5mm_Horizontal', 'description': 'Omron FPC connector, 40 top-side contacts, 0.5mm pitch, SMT, https://omronfs.omron.com/en_US/ecb/products/pdf/en-xf2m.pdf', 'tags': 'omron fpc xf2m', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_FFC-FPC.3dshapes/Omron_XF2M-4015-1A-1MP_P0.5mm_Horizontal.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_FFC-FPC : Omron_XF2M-4015-1A_1x40-1MP_P0.5mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

