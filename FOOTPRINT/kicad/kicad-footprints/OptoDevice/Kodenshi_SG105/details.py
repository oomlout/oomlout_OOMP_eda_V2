
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Kodenshi_SG105"
    hexID = "FZKOPKODENSHISG15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Kodenshi_SG105', 'description': 'package for Kodenshi SG-105 with PCB cutout, light-direction upwards, see http://www.kodenshi.co.jp/products/pdf/sensor/photointerrupter_ref/SG-105.pdf', 'tags': 'refective opto couple photo coupler', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Kodenshi_SG105.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('OptoDevice : Kodenshi_SG105')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

