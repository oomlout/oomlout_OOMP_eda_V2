
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Resonator_SMD_Murata_CSTxExxV-3Pin_3.0x1.1mm_HandSoldering"
    hexID = "FZKXRSCSTXEXXV3PIN3X11HANDSOLDERING"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Resonator_SMD_Murata_CSTxExxV-3Pin_3.0x1.1mm_HandSoldering', 'description': 'SMD Resomator/Filter Murata CSTCE, https://www.murata.com/en-eu/products/productdata/8801162264606/SPEC-CSTNE16M0VH3C000R0.pdf', 'tags': 'SMD SMT ceramic resonator filter', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator_SMD_Murata_CSTxExxV-3Pin_3.0x1.1mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Crystal : Resonator_SMD_Murata_CSTxExxV-3Pin_3.0x1.1mm_HandSoldering')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

