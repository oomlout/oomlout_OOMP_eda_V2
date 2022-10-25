
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Everlight_ITR8307_Reverse"
    hexID = "FZKOPEVERLIGHTITR837R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Everlight_ITR8307_Reverse', 'description': 'package for Everlight ITR8307 with PCB cutout, light-direction downwards, see http://www.everlight.com/file/ProductFile/ITR8307.pdf', 'tags': 'refective opto couple photo coupler', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Everlight_ITR8307_Reverse.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Everlight_ITR8307_Reverse')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

