
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_RJ"
    oIndex = "RJ14_Connfly_DS1133-S4_Horizontal"
    hexID = "FZKCNRJRJ14CONNFLYDS1133S4HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RJ14_Connfly_DS1133-S4_Horizontal', 'description': 'RJ14 connector 6P4C Horizontal http://www.connfly.com/userfiles/image/UpLoadFile/File/2012/10/26/DS1133.pdf', 'tags': 'RJ14 connector 6P4C Connfly DS1133', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ14_Connfly_DS1133-S4_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_RJ : RJ14_Connfly_DS1133-S4_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

