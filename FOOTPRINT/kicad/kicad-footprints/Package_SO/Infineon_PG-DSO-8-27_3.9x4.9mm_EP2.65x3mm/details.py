
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "Infineon_PG-DSO-8-27_3.9x4.9mm_EP2.65x3mm"
    hexID = "FZKSOINFINEONPGDSO82739X49EP265X3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_PG-DSO-8-27_3.9x4.9mm_EP2.65x3mm', 'description': 'Infineon  PG-DSO, 8 Pin (https://www.infineon.com/cms/en/product/packages/PG-DSO/PG-DSO-8-27), generated with kicad-footprint-generator ipc_gullwing_generator.py', 'tags': 'Infineon PG-DSO SO', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/Infineon_PG-DSO-8-27_3.9x4.9mm_EP2.65x3mm.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Package_SO : Infineon_PG-DSO-8-27_3.9x4.9mm_EP2.65x3mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

