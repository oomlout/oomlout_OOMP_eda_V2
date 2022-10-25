
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Socket"
    oIndex = "Wells_648-0482211SA01"
    hexID = "FZKSOWELLS648482211SA1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Wells_648-0482211SA01', 'description': 'https://www.farnell.com/cad/316865.pdf?_ga=2.37208032.177107060.1530611323-249019997.1498114824', 'tags': '48pin TSOP Socket', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Socket.3dshapes/Wells_648-0482211SA01.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Socket : Wells_648-0482211SA01')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

