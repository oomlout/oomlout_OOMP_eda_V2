
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "MSOP-8-1EP_3x3mm_P0.65mm_EP1.73x1.85mm_ThermalVias"
    hexID = "FZKSOMS81EP3X3P65EP173X185THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'MSOP-8-1EP_3x3mm_P0.65mm_EP1.73x1.85mm_ThermalVias', 'description': 'MSOP, 8 Pin (http://www.ti.com/lit/ds/symlink/lm25085.pdf#page=32), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'MSOP SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/MSOP-8-1EP_3x3mm_P0.65mm_EP1.73x1.85mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : MSOP-8-1EP_3x3mm_P0.65mm_EP1.73x1.85mm_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

