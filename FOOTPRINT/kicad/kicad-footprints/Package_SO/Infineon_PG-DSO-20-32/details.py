
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "Infineon_PG-DSO-20-32"
    hexID = "FZKSOINFINEONPGDSO232"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_PG-DSO-20-32', 'description': 'Infineon SO package 20pin without exposed pad (https://www.infineon.com/cms/en/product/packages/PG-DSO/PG-DSO-20-32/)', 'tags': 'DSO-20', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/Infineon_PG-DSO-20-32.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : Infineon_PG-DSO-20-32')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

