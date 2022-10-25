
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_TO_SOT_SMD"
    oIndex = "Vishay_PowerPAK_SC70-6L_Dual"
    hexID = "FZKPACKAGETOSOTSMVISHAYPOWERPAKSC76LDUAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Vishay_PowerPAK_SC70-6L_Dual', 'description': 'Vishay PowerPAK SC70 dual transistor package http://www.vishay.com/docs/70487/70487.pdf', 'tags': 'powerpak sc70 sc-70 dual', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/Vishay_PowerPAK_SC70-6L_Dual.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_TO_SOT_SMD : Vishay_PowerPAK_SC70-6L_Dual')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

