
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "MSOP-12-16-1EP_3x4mm_P0.5mm_EP1.65x2.85mm_ThermalVias"
    hexID = "FZKSOMS12161EP3X4P5EP165X285THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MSOP-12-16-1EP_3x4mm_P0.5mm_EP1.65x2.85mm_ThermalVias', 'description': '10-Lead Plastic Micro Small Outline Package (MS) [MSOP] (see Microchip Packaging Specification 00000049BS.pdf)', 'tags': 'SSOP 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/MSOP-12-16-1EP_3x4mm_Pitch0.5mm_EP1.65x2.85mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : MSOP-12-16-1EP_3x4mm_P0.5mm_EP1.65x2.85mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

