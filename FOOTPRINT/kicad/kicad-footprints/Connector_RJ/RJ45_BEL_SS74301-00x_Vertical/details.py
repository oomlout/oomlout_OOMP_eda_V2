
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_RJ"
    oIndex = "RJ45_BEL_SS74301-00x_Vertical"
    hexID = "FZKCNRJRJ45BELSS7431XVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RJ45_BEL_SS74301-00x_Vertical', 'description': 'https://belfuse.com/resources/drawings/stewartconnector/dr-stw-ss-74301-001-ss-74301-002-ss-74301-005.pdf', 'tags': 'RJ45 Vertical Shield LED Green Yellow', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_BEL_SS74301-00x_Vertical.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_RJ : RJ45_BEL_SS74301-00x_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

