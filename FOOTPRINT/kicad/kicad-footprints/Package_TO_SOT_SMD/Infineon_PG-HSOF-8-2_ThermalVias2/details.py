
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_SMD"
    oIndex = "Infineon_PG-HSOF-8-2_ThermalVias2"
    hexID = "FZKPACKAGETOSOTSMINFINEONPGHSOF82THERMALVIAS2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Infineon_PG-HSOF-8-2_ThermalVias2', 'description': 'HSOF-8-2 [TOLL] power MOSFET (http://www.infineon.com/cms/en/product/packages/PG-HSOF/PG-HSOF-8-2/, https://www.infineon.com/dgdl/Infineon-ApplicationNote_600V_CoolMOS_C7_Gold_TOLL-AN-v01_00-EN.pdf?fileId=5546d4625b10283a015b144a1af70df6)', 'tags': 'mosfet hsof toll thermal vias', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/Infineon_PG-HSOF-8-2.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_SMD : Infineon_PG-HSOF-8-2_ThermalVias2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

