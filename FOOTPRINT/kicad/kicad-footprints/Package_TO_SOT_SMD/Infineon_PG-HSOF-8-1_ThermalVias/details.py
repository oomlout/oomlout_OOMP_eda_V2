
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_SMD"
    oIndex = "Infineon_PG-HSOF-8-1_ThermalVias"
    hexID = "FZKPACKAGETOSOTSMINFINEONPGHSOF81THERMALVIAS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_PG-HSOF-8-1_ThermalVias', 'description': 'HSOF-8-1 [TOLL] power MOSFET (http://www.infineon.com/cms/en/product/packages/PG-HSOF/PG-HSOF-8-1/)', 'tags': 'mosfet hsof toll thermal vias', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/Infineon_PG-HSOF-8-1.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_TO_SOT_SMD : Infineon_PG-HSOF-8-1_ThermalVias')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

