
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "Infineon_PG-DSO-12-11_ThermalVias"
    hexID = "FZKSOINFINEONPGDSO1211THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_PG-DSO-12-11_ThermalVias', 'description': 'Infineon PG-DSO 12 pin, exposed pad: 4.5x8.1mm, with thermal vias (https://www.infineon.com/cms/en/product/packages/PG-DSO/PG-DSO-12-11/)', 'tags': 'PG-DSO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/Infineon_PG-DSO-12-11.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : Infineon_PG-DSO-12-11_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

