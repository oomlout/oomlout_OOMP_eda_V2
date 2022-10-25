
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Audio"
    oIndex = "Jack_3.5mm_QingPu_WQP-PJ398SM_Vertical_CircularHoles"
    hexID = "FZKCNAUDIOJ35QINGPUWQPPJ398SMVERTICALCIRCULARH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Jack_3.5mm_QingPu_WQP-PJ398SM_Vertical_CircularHoles', 'description': 'TRS 3.5mm, vertical, Thonkiconn, PCB mount, (http://www.qingpu-electronics.com/en/products/WQP-PJ398SM-362.html)', 'tags': 'WQP-PJ398SM WQP-PJ301M-12 TRS 3.5mm mono vertical jack thonkiconn qingpu', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_3.5mm_QingPu_WQP-PJ398SM_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Connector_Audio : Jack_3.5mm_QingPu_WQP-PJ398SM_Vertical_CircularHoles')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

