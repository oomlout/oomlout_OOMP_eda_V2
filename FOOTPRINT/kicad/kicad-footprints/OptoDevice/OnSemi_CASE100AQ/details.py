
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "OnSemi_CASE100AQ"
    hexID = "FZKOPONSEMICASE1AQ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'OnSemi_CASE100AQ', 'description': 'OnSemi CASE 100AQ for QRE1113, see https://www.onsemi.com/pub/Collateral/QRE1113-D.PDF', 'tags': 'reflective opto couple photo coupler', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/OnSemi_CASE100AQ.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : OnSemi_CASE100AQ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

