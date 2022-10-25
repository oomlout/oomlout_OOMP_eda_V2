
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Coaxial"
    oIndex = "BNC_Win_364A2x95_Horizontal"
    hexID = "FZKCNCOABNCWIN364A2X95HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'BNC_Win_364A2x95_Horizontal', 'description': 'Dual front isolated BNC plug (https://www.winconn.com/wp-content/uploads/364A2595.pdf)', 'tags': 'Dual BNC Horizontal Isolated', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/BNC_Win_364A2x95_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Connector_Coaxial : BNC_Win_364A2x95_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

