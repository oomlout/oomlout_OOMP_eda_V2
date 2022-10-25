
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_JAE"
    oIndex = "JAE_MM70-314-310B1"
    hexID = "FZKCNJAEJAE731431B1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'JAE_MM70-314-310B1', 'description': 'http://www.heilind.com/marketing/documents/jae/JAE_MM70.pdf', 'tags': 'connector JAE MXM', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_JAE.3dshapes/JAE_MM70-314-310B1.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_JAE : JAE_MM70-314-310B1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

