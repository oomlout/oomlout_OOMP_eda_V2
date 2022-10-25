
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_RJ"
    oIndex = "RJ25_Wayconn_MJEA-660X1_Horizontal"
    hexID = "FZKCNRJRJ25WAYCONNMJEA66X1HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'RJ25_Wayconn_MJEA-660X1_Horizontal', 'description': 'RJ25 6P6C Socket 90 degrees, https://wayconn.com/wp-content/themes/way/datasheet/MJEA-660X1XXX_RJ25_6P6C_PCB_RA.pdf', 'tags': 'RJ12 RJ18 RJ25 jack connector 6P6C', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ25_Wayconn_MJEA-660X1_Horizontal.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Connector_RJ : RJ25_Wayconn_MJEA-660X1_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

