
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "OptoDevice"
    oIndex = "Lightpipe_LPF-C013301S"
    hexID = "FZKOPLIGHTPIPELPFC1331S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Lightpipe_LPF-C013301S', 'description': 'https://www.lumex.com/spec/LPF-C013301S.pdf', 'tags': 'lightpipe triple tower right angle 3mm', 'attributeType': None, 'threeDModel': '${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/Lightpipe_LPF-C013301S.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('OptoDevice : Lightpipe_LPF-C013301S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

