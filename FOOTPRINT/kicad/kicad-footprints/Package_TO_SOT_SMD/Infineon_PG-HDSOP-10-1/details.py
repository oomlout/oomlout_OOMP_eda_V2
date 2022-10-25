
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_SMD"
    oIndex = "Infineon_PG-HDSOP-10-1"
    hexID = "FZKPACKAGETOSOTSMINFINEONPGHDS11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_PG-HDSOP-10-1', 'description': 'Infineon PG-HDSOP-10-1 (DDPAK), 20.96x6.5x2.3mm, slug up (https://www.infineon.com/cms/en/product/packages/PG-HDSOP/PG-HDSOP-10-1/)', 'tags': 'hdsop 10 ddpak', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/Infineon_PG-HDSOP-10-1.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_SMD : Infineon_PG-HDSOP-10-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

