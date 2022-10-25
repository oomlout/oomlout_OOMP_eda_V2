
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "3-SIP_Module_V7805-1000"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTS3SIPMOV7851"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': '3-SIP_Module_V7805-1000', 'description': 'http://www.cui.com/product/resource/v78xx-1000.pdf', 'tags': None, 'attributeType': None, 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('digikey-footprints : 3-SIP_Module_V7805-1000')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

