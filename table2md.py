import os

tabStr = '''
<table>
    <thead>
        <tr>
            <th>
                <p>符号</p>
            </th>
            <th>
                <p>含义</p>
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <p>i</p>
            </td>
            <td>
                <p>-1的平方根</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>f(x)</p>
            </td>
            <td>
                <p>函数f在自变量x处的值</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>sin(x)</p>
            </td>
            <td>
                <p>在自变量x处的正弦函数值</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>exp(x)</p>
            </td>
            <td>
                <p>在自变量x处的指数函数值，常被写作ex</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>a^x</p>
            </td>
            <td>
                <p>a的x次方；有理数x由反函数定义</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ln x</p>
            </td>
            <td>
                <p>exp x 的反函数</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ax</p>
            </td>
            <td>
                <p>同 a^x</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>logba</p>
            </td>
            <td>
                <p>以b为底a的对数； blogba = a</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>cos x</p>
            </td>
            <td>
                <p>在自变量x处余弦函数的值</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>tan x</p>
            </td>
            <td>
                <p>其值等于 sin x/cos x</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>cot x</p>
            </td>
            <td>
                <p>余切函数的值或 cos x/sin x</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>sec x</p>
            </td>
            <td>
                <p>正割含数的值，其值等于 1/cos x</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>csc x</p>
            </td>
            <td>
                <p>余割函数的值，其值等于 1/sin x</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>asin x</p>
            </td>
            <td>
                <p>y，正弦函数反函数在x处的值，即 x = sin y</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>acos x</p>
            </td>
            <td>
                <p>y，余弦函数反函数在x处的值，即 x = cos y</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>atan x</p>
            </td>
            <td>
                <p>y，正切函数反函数在x处的值，即 x = tan y</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>acot x</p>
            </td>
            <td>
                <p>y，余切函数反函数在x处的值，即 x = cot y</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>asec x</p>
            </td>
            <td>
                <p>y，正割函数反函数在x处的值，即 x = sec y</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>acsc x</p>
            </td>
            <td>
                <p>y，余割函数反函数在x处的值，即 x = csc y</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>θ</p>
            </td>
            <td>
                <p>角度的一个标准符号，不注明均指弧度，尤其用于表示atan x/y，当x、y、z用于表示空间中的点时</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>i, j, k</p>
            </td>
            <td>
                <p>分别表示x、y、z方向上的单位向量</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>(a, b, c)</p>
            </td>
            <td>
                <p>以a、b、c为元素的向量</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>(a, b)</p>
            </td>
            <td>
                <p>以a、b为元素的向量</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>(a, b)</p>
            </td>
            <td>
                <p>a、b向量的点积</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>a•b</p>
            </td>
            <td>
                <p>a、b向量的点积</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>(a•b)</p>
            </td>
            <td>
                <p>a、b向量的点积</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>|v|</p>
            </td>
            <td>
                <p>向量v的模</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>|x|</p>
            </td>
            <td>
                <p>数x的绝对值</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>Σ</p>
            </td>
            <td>
                <p>表示求和，通常是某项指数。下边界值写在其下部，上边界值写在其上部。如j从1到100 的和可以表示成：。这表示 1 + 2 + … + n</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>M</p>
            </td>
            <td>
                <p>表示一个矩阵或数列或其它</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>|v&gt;</p>
            </td>
            <td>
                <p>列向量，即元素被写成列或可被看成k×1阶矩阵的向量</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>&lt;v|</p>
            </td>
            <td>
                <p>被写成行或可被看成从1×k阶矩阵的向量</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>dx</p>
            </td>
            <td>
                <p>变量x的一个无穷小变化，dy, dz, dr等类似</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ds</p>
            </td>
            <td>
                <p>长度的微小变化</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ρ</p>
            </td>
            <td>
                <p>变量 (x2 + y2 + z2)1/2 或球面坐标系中到原点的距离</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>r</p>
            </td>
            <td>
                <p>变量 (x2 + y2)1/2 或三维空间或极坐标中到z轴的距离</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>|M|</p>
            </td>
            <td>
                <p>矩阵M的行列式，其值是矩阵的行和列决定的平行区域的面积或体积</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>||M||</p>
            </td>
            <td>
                <p>矩阵M的行列式的值，为一个面积、体积或超体积</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>det M</p>
            </td>
            <td>
                <p>M的行列式</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>M-1</p>
            </td>
            <td>
                <p>矩阵M的逆矩阵</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>v×w</p>
            </td>
            <td>
                <p>向量v和w的向量积或叉积</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>θvw</p>
            </td>
            <td>
                <p>向量v和w之间的夹角</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>A•B×C</p>
            </td>
            <td>
                <p>标量三重积，以A、B、C为列的矩阵的行列式</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>uw</p>
            </td>
            <td>
                <p>在向量w方向上的单位向量，即 w/|w|</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>df</p>
            </td>
            <td>
                <p>函数f的微小变化，足够小以至适合于所有相关函数的线性近似</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>df/dx</p>
            </td>
            <td>
                <p>f关于x的导数，同时也是f的线性近似斜率</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>f '</p>
            </td>
            <td>
                <p>函数f关于相应自变量的导数，自变量通常为x</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>∂f/∂x</p>
            </td>
            <td>
                <p>y、z固定时f关于x的偏导数。通常f关于某变量q的偏导数为当其它几个变量固定时df 与dq的比值。任何可能导致变量混淆的地方都应明确地表述</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>(∂f/∂x)|r,z</p>
            </td>
            <td>
                <p>保持r和z不变时，f关于x的偏导数</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>grad f</p>
            </td>
            <td>
                <p>元素分别为f关于x、y、z偏导数 [(∂f/∂x), (∂f/∂y), (∂f/∂z)] 或 (∂f/∂x)i + (∂f/∂y)j + (∂f/∂z)k; 的向量场，称为f的梯度</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>∇</p>
            </td>
            <td>
                <p>向量算子(∂/∂x)i + (∂/∂x)j + (∂/∂x)k, 读作 "del"</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>∇f</p>
            </td>
            <td>
                <p>f的梯度；它和 uw 的点积为f在w方向上的方向导数</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>∇•w</p>
            </td>
            <td>
                <p>向量场w的散度，为向量算子∇&nbsp;同向量 w的点积, 或 (∂wx /∂x) + (∂wy /∂y) + (∂wz /∂z)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>curl w</p>
            </td>
            <td>
                <p>向量算子 ∇&nbsp;同向量 w 的叉积</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>∇×w</p>
            </td>
            <td>
                <p>w的旋度，其元素为[(∂fz /∂y) - (∂fy /∂z), (∂fx /∂z) - (∂fz /∂x), (∂fy /∂x) - (∂fx /∂y)]</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>∇•∇</p>
            </td>
            <td>
                <p>拉普拉斯微分算子： (∂2/∂x2) + (∂/∂y2) + (∂/∂z2)</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>f "(x)</p>
            </td>
            <td>
                <p>f关于x的二阶导数，f '(x)的导数</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>d2f/dx2</p>
            </td>
            <td>
                <p>f关于x的二阶导数</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>f(2)(x)</p>
            </td>
            <td>
                <p>同样也是f关于x的二阶导数</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>f(k)(x)</p>
            </td>
            <td>
                <p>f关于x的第k阶导数，f(k-1) (x)的导数</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>T</p>
            </td>
            <td>
                <p>曲线切线方向上的单位向量，如果曲线可以描述成 r(t), 则T = (dr/dt)/|dr/dt|</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ds</p>
            </td>
            <td>
                <p>沿曲线方向距离的导数</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>κ</p>
            </td>
            <td>
                <p>曲线的曲率，单位切线向量相对曲线距离的导数的值：|dT/ds|</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>N</p>
            </td>
            <td>
                <p>dT/ds投影方向单位向量，垂直于T</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>B</p>
            </td>
            <td>
                <p>平面T和N的单位法向量，即曲率的平面</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>τ</p>
            </td>
            <td>
                <p>曲线的扭率： |dB/ds|</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>g</p>
            </td>
            <td>
                <p>重力常数</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>F</p>
            </td>
            <td>
                <p>力学中力的标准符号</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>k</p>
            </td>
            <td>
                <p>弹簧的弹簧常数</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>pi</p>
            </td>
            <td>
                <p>第i个物体的动量</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>H</p>
            </td>
            <td>
                <p>物理系统的哈密尔敦函数，即位置和动量表示的能量</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>{Q, H}</p>
            </td>
            <td>
                <p>Q, H的泊松括号</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>&nbsp;</p>
            </td>
            <td>
                <p>以一个关于x的函数的形式表达的f(x)的积分</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>&nbsp;</p>
            </td>
            <td>
                <p>函数f 从a到b的定积分。当f是正的且 a &lt; b 时表示由x轴和直线y = a, y = b 及在这些直线之间的函数曲线所围起来图形的面积</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>L(d)</p>
            </td>
            <td>
                <p>相等子区间大小为d，每个子区间左端点的值为 f的黎曼和</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>R(d)</p>
            </td>
            <td>
                <p>相等子区间大小为d，每个子区间右端点的值为 f的黎曼和</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>M(d)</p>
            </td>
            <td>
                <p>相等子区间大小为d，每个子区间上的最大值为 f的黎曼和</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>m(d)</p>
            </td>
            <td>
                <p>相等子区间大小为d，每个子区间上的最小值为 f的黎曼和</p>
            </td>
        </tr>
    </tbody>
</table>
'''
# tabStr = '''
#   <table>
#     <tbody>
#       <tr>
#         <td>
#         <p>符号</p>
#         </td>

#         <td>
#         <p>符号2</p>
#         </td>
#       </tr>
#     </tbody>
#   </table>

# '''
#
# | Tables        | Are           | Cool  |
# | ------------- |:-------------:| -----:|
# | col 3 is      | right-aligned | $1600 |
# | col 2 is      | centered      |   $12 |
# | zebra stripes | are neat      |    $1 |

divStr = ":-------------:"
maxTdSpace = len(divStr)

# tdStr:td的内容,并且判断中文的个数,因为一个中文和一个字符的len是相同的


def getTdRemainSpaceCount(tdStr):
  charCount = len(tdStr)
  hanziCharCount = 0
  for index in range(0, charCount):
    # 如果是汉字
    if(u'\u4e00' <= tdStr[index] <= u'\u9fff'):
      hanziCharCount += 1
  return maxTdSpace - len(tdStr) - hanziCharCount


def getSpaceStr(spaceCount):
  spaceStr = ""
  for i in range(0, spaceCount):
    spaceStr += " "
  return spaceStr

# 打印一行(一个 <tr>)   targetPreSplitStr 可能为 <td style="text-align: center">, targetBackSplitStr是 </th> 或 </td>


def printTabRow(str, targetPreSplitStr, targetBackSplitStr):
  '''
  处理每行中的单元格
  '''
  rawCount = str.count(targetBackSplitStr, 0, len(str))
  splitStr = str
  for index in range(0, rawCount):
    # print("for 循环 splitStr=" + splitStr)
    backIndex = splitStr.find(targetBackSplitStr)
    preStr = splitStr[0:backIndex].strip()
    targetPreIndex = preStr.find(targetPreSplitStr)
    splitedStr = preStr[targetPreIndex:backIndex].strip()
    preIndex = splitedStr.find(">") + 1
    targetStr = splitedStr[preIndex:backIndex].strip()
    # print(
    #     # 'backIndex', backIndex,
    #     'preStr:', preStr,
    #     # ',',
    #     # 'targetPreIndex', targetPreIndex,
    #     # '------------',
    #     'splitedStr:', splitedStr,
    #     # ',',
    #     # 'preIndex', preIndex,
    #     # '------------',
    #     'targetStr', targetStr,
    #     #     '------------'
    # )
    if index == 0:
      print("|", end='')

    remainPreSpaceCount = 0
    remainBackSpaceCount = 0
    tempRemainSpaceCount = getTdRemainSpaceCount(targetStr)
    if tempRemainSpaceCount % 2 == 0:
      remainPreSpaceCount = int(tempRemainSpaceCount / 2)
      remainBackSpaceCount = remainPreSpaceCount
    else:
      remainPreSpaceCount = int(tempRemainSpaceCount / 2)
      remainBackSpaceCount = remainPreSpaceCount + 1

    preSpaceStr = getSpaceStr(remainPreSpaceCount)
    backSpaceStr = getSpaceStr(remainBackSpaceCount)
    # 将 strong 标签替换掉
    targetStr = targetStr.replace("<strong>", "**")
    targetStr = targetStr.replace("</strong>", "**")
    print(preSpaceStr + '```' + targetStr + '```' + backSpaceStr + "|", end='')
    # print(
    #     '-------'
    #     # 'preSpaceStr',preSpaceStr,
    # 'splitedStr', splitedStr,
    #     # 'targetStr', targetStr,
    #     # 'backSpaceStr', backSpaceStr
    # )
    splitStr = splitStr[backIndex + len(targetBackSplitStr):len(str)]
    # print("for 循环，截取 splitStr=" + splitStr)
  print("")  # 如果要是 print("\n")反而会换两行

# divCount 是格数


def printTabDivision(divCount):
  for index in range(0, divCount):
    if index == 0:
      print("|", end='')
    print(divStr + "|", end='')
  print("")


# 解析 thead
tHeadPreIndex = tabStr.find('<thead>') + len('<thead>')
tHeadBackIndex = tabStr.find('</thead>')
tHeadStr = tabStr[tHeadPreIndex:tHeadBackIndex].replace(
    '<p>', '').replace('</p>', '').strip('')
# print("tHeadStr=" + tHeadStr)
printTabRow(tHeadStr, "<th>", "</th>")
divCount = tHeadStr.count("</th>", 0, len(tHeadStr))
printTabDivision(divCount)

# 解析 tbody
tbodyPreIndex = tabStr.find('<tbody>') + len('<tbody>')
tbodyBackIndex = tabStr.find('</tbody>')
tbodyStr = tabStr[tbodyPreIndex:tbodyBackIndex]
trCount = tbodyStr.count("</tr>", 0, len(tbodyStr))

tempTbodyStr = tbodyStr
for index in range(0, trCount):
  lastTrIndex = tempTbodyStr.find("</tr>") + len("</tr>")
  preTrIndex = tempTbodyStr.find("<tr>")
  targetTrStr = tempTbodyStr[preTrIndex:lastTrIndex]
  # print(
  #     'targetTrStr', targetTrStr
  # )
  targetTrStr = targetTrStr.replace('<p>', '')
  targetTrStr = targetTrStr.replace('</p>', '')
  targetTrStr = targetTrStr.strip('')
  # print('----------->', targetTrStr, '<-----------')
  printTabRow(targetTrStr, "<td>", "</td>")
  tempTbodyStr = tempTbodyStr[lastTrIndex:len(tempTbodyStr)]

os.system("pause")
