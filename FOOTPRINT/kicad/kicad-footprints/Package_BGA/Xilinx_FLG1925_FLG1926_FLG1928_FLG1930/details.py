
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Xilinx_FLG1925_FLG1926_FLG1928_FLG1930"
    hexID = "FZKBGAXILINXFLG1925FLG1926FLG1928FLG193"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Xilinx_FLG1925_FLG1926_FLG1928_FLG1930', 'description': 'Virtex-7 BGA, 44x44 grid, 45x45mm package, 1mm pitch; https://www.xilinx.com/support/documentation/user_guides/ug475_7Series_Pkg_Pinout.pdf#page=304, NSMD pad definition Appendix A', 'tags': 'BGA 1924 1 FL1925 FLG1925 FL1926 FLG1926 FL1928 FLG1928 FL1930 FLG1930', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Xilinx_FLG1925_FLG1926_FLG1928_FLG1930.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Xilinx_FLG1925_FLG1926_FLG1928_FLG1930')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

