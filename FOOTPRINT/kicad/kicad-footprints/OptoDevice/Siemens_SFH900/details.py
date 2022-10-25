
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Siemens_SFH900"
    hexID = "FZKOPSIEMENSSFH9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Siemens_SFH900', 'description': 'package for Siemens SFH900 reflex photo interrupter/coupler/object detector, see https://www.batronix.com/pdf/sfh900.pdf', 'tags': 'Siemens SFH900 reflex photo interrupter coupler object detector', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Siemens_SFH900.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Siemens_SFH900')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

