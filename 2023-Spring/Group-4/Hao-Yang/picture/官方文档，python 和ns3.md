# 使用python 运行ns-3?


python 绑定允许从 Python 调用 ns-3 中的C++代码。

本章介绍如何创建可以运行 ns-3 的 Python 脚本，以及为 C++ ns-3 模块创建 Python 绑定的过程。

运行 Pyviz 可视化工具也需要 Python 绑定。

Python 绑定支持将 ns-3 模型库导入为 Python 模块。提供了大多数 ns-3 C++ API 的覆盖范围。意图 一直允许程序员编写完整的模拟脚本 Python，允许将ns-3与其他Python工具和工作流程集成。 目的不是提供不同的语言选择来编写在 Python 中实现的新 ns-3 模型。ns-3使用了一个名为Cppyy的工具来创建Python绑定。Cppyy是一个工具，它通过导入C++库和头文件来在运行时构建Python绑定，从而生成一个Python模块。这意味着，即使C++ API发生变化，Python绑定也会相应适应这些变化，而无需进行任何预处理或扫描操作。

在ns-3.37版本之前，ns-3中使用的Python绑定框架是Pybindgen。Pybindgen是一个用于生成C++和Python之间绑定代码的工具。它可以帮助将C++库暴露给Python，使得可以在Python中调用和使用这些C++库的功能。然而，在ns-3.37版本之后，该框架被Cppyy取代，成为了ns-3的新的Python绑定框架。

一个使用Python编写的脚本，它通过调用ns-3库函数来运行ns-3网络模拟器。这个示例脚本可能包含了创建网络拓扑、配置网络参数、设置应用程序等操作，以便模拟特定的网络场景。

通过这个示例脚本，您可以了解如何使用Python编写脚本来与ns-3进行交互，并通过调用ns-3的功能来构建和运行网络模拟。这个示例脚本可能包含了使用ns-3的API来创建节点、设置链路、配置网络协议栈、添加应用程序等操作，以实现特定的网络模拟目标。


```python
from ns import ns

ns.core.LogComponentEnable("UdpEchoClientApplication", ns.core.LOG_LEVEL_INFO)
ns.core.LogComponentEnable("UdpEchoServerApplication", ns.core.LOG_LEVEL_INFO)

nodes = ns.network.NodeContainer()
nodes.Create(2)

pointToPoint = ns.point_to_point.PointToPointHelper()
pointToPoint.SetDeviceAttribute("DataRate", ns.core.StringValue("5Mbps"))
pointToPoint.SetChannelAttribute("Delay", ns.core.StringValue("2ms"))

devices = pointToPoint.Install(nodes)

stack = ns.internet.InternetStackHelper()
stack.Install(nodes)

address = ns.internet.Ipv4AddressHelper()
address.SetBase(ns.network.Ipv4Address("10.1.1.0"),
                ns.network.Ipv4Mask("255.255.255.0"))

interfaces = address.Assign(devices)

echoServer = ns.applications.UdpEchoServerHelper(9)

serverApps = echoServer.Install(nodes.Get(1))
serverApps.Start(ns.core.Seconds(1.0))
serverApps.Stop(ns.core.Seconds(10.0))

address = interfaces.GetAddress(1).ConvertTo()
echoClient = ns.applications.UdpEchoClientHelper(address, 9)
echoClient.SetAttribute("MaxPackets", ns.core.UintegerValue(1))
echoClient.SetAttribute("Interval", ns.core.TimeValue(ns.core.Seconds(1.0)))
echoClient.SetAttribute("PacketSize", ns.core.UintegerValue(1024))

clientApps = echoClient.Install(nodes.Get(0))
clientApps.Start(ns.core.Seconds(2.0))
clientApps.Stop(ns.core.Seconds(10.0))

ns.core.Simulator.Run()
ns.core.Simulator.Destroy()
```

运行python 脚本

首先检验cppyy是否已安装，导入cppyy模块查看是否成功
cppyy是一个用于在python 中调用C++代码的库，可执行下列导语，判断是否安装成功，若没有，记得用pip安装


```python
import cppyy
```


```python
python3 -m pip install --user cppyy
```

首先启用python 连接


```python
./ns3 configure --enable-python-bindings
```

使用ns-3运行实例的两种方法

第一种方法是运行一个ns3 shell。ns3 shell是一个交互式环境，类似于Python shell，它已经配置好了ns3模块的路径和环境。您可以在ns3 shell中直接运行示例程序。这样，ns3会自动处理Python路径设置，使得示例程序可以正确地找到和导入ns3模块


```python
./ns3 shell
 python3 examples/wireless/mixed-wireless.py
```

第二种方法是在构建和安装ns3之后，手动配置Python路径，以便能够找到ns3模块。您可以将ns3模块所在的路径添加到Python的sys.path中，这样示例程序就能够正确地导入ns3模块


```python
./ns3 run examples/wireless/mixed-wireless.py
```

在不进行项目重建的情况下运行程序，反复运行同一个程序使用不同的参数，用下面这个可以提高执行时间


```python
./ns3 run --no-build examples/wireless/mixed-wireless.py
```

在C调试器下运行python 脚本文件


```python
./ns3 shell
gdb --args python3 examples/wireless/mixed-wireless.py
```

要运行自己的调用 ns-3 且具有此路径的 Python 脚本，请执行以下操作：/path/to/your/example/my-script.py

## Python 并非 100% 支持 API。其中一些原因是：

### 内存管理问题

一些 API 涉及指针，这需要知道哪种内存传递语义（谁拥有什么内存）。 这些知识不是函数签名的一部分，要么有记录，要么有时甚至没有记录。 您可能需要通过使用实时 （JIT） 编译函数在C++端实例化变量来解决这些问题。

例如，在处理命令行参数时，我们可以设置其他参数，如以下代码所示：


```python
# Import the ns-3 C++ modules with Cppyy
from ns import ns

# To pass the addresses of the Python variables to c++, we need to use ctypes
from ctypes import c_bool, c_int, c_double, c_char_p, create_string_buffer
verbose = c_bool(True)
nCsma = c_int(3)
throughputKbps = c_double(3.1415)
BUFFLEN = 4096
outputFileBuffer = create_string_buffer(b"default_output_file.xml", BUFFLEN)
outputFile = c_char_p(outputFileBuffer.raw)

# Cppyy will transform the ctype types into the appropriate reference or raw pointers
cmd = ns.CommandLine(__file__)
cmd.AddValue("verbose", "Tell echo applications to log if true", verbose)
cmd.AddValue("nCsma", "Number of extra CSMA nodes/devices", nCsma)
cmd.AddValue("throughputKbps", "Throughput of nodes", throughputKbps)
cmd.AddValue("outputFile", "Output file name", outputFile, BUFFLEN)
cmd.Parse(sys.argv)

# Printing values of the different ctypes passed as arguments post parsing
print("Verbose:", verbose.value)
print("nCsma:", nCsma.value)
print("throughputKbps:", throughputKbps.value)
print("outputFile:", outputFile.value)
```

请注意，变量作为引用或原始指针传递。在 Python 端重新分配它们 （例如 ）可能导致 Python 垃圾回收器破坏对象 因为它的唯一引用已被覆盖，允许垃圾回收器回收该内存空间。 然后，C++端将有一个对变量的悬空引用，可以用 意外值，稍后可以读取，导致 NS-3 由于内存损坏而行为异常。verbose = verbose.value

字符串值是有问题的，因为 Python 和C++字符串生存期的处理方式不同。 为了解决这个问题，我们需要使用以 null 结尾的 C 字符串 （） 在 绑定和 NS-3 模块库。但是，C 字符串特别危险，因为 覆盖 null 终止符也可能导致内存损坏。传递 C 字符串时，请记住 以分配大型缓冲区并尽可能执行边界检查。命令行：：添加值 的变量执行边界检查并在解析值的情况下中止执行 不适合缓冲区。确保传递缓冲区的完整大小，包括 null 终止符。char*char*

下面是一个示例，演示了在存在内存损坏的情况下如何发生 命令行中的无边界检查：添加值变体。char*


```python
from ns import ns
from ctypes import c_char_p, c_char, create_string_buffer, byref, cast

# The following buffer represent the memory contents
# of a program containing two adjacent C strings
# This could be the result of two subsequent variables
# on the stack or dynamically allocated
memoryContents = create_string_buffer(b"SHORT_STRING_CONTENTS\0"+b"DoNotWriteHere_"*5+b"\0")
lenShortString = len(b"SHORT_STRING_CONTENTS\0")

# In the next lines, we pick pointers to these two C strings
shortStringBuffer = cast(byref(memoryContents, 0), c_char_p)
victimBuffer = cast(byref(memoryContents, lenShortString), c_char_p)

cmd = ns.core.CommandLine(__file__)
# in the real implementation, the buffer size of 21+1 bytes containing SHORT_STRING_CONTENTS\0 is passed
cmd.AddValue("shortString", "", shortStringBuffer)

print("Memory contents before the memory corruption")
print("Full Memory contents", memoryContents.raw)
print("shortStringBuffer contents: ", shortStringBuffer.value)
print("victimBuffer contents: ", victimBuffer.value)

# The following block should print to the terminal.
# Note that the strings are correctly
# identified due to the null terminator (\x00)
#
# Memory contents before the memory corruption
# Full Memory contents b'SHORT_STRING_CONTENTS\x00DoNotWriteHere_DoNotWriteHere_DoNotWriteHere_DoNotWriteHere_DoNotWriteHere_\x00\x00'
# shortStringBuffer size=21, contents: b'SHORT_STRING_CONTENTS'
# victimBuffer size=75, contents: b'DoNotWriteHere_DoNotWriteHere_DoNotWriteHere_DoNotWriteHere_DoNotWriteHere_'

# Write a very long string to a small buffer of size lenShortString = 22
cmd.Parse(["python", "--shortString="+("OkToWrite"*lenShortString)[:lenShortString]+"CORRUPTED_"*3])

print("\n\nMemory contents after the memory corruption")
print("Full Memory contents", memoryContents.raw)
print("shortStringBuffer contents: ", shortStringBuffer.value)
print("victimBuffer contents: ", victimBuffer.value)

# The following block should print to the terminal.
#
# Memory contents after the memory corruption
# Full Memory contents b'OkToWriteOkToWriteOkToCORRUPTED_CORRUPTED_CORRUPTED_\x00oNotWriteHere_DoNotWriteHere_DoNotWriteHere_\x00\x00'
# shortStringBuffer size=52, contents: b'OkToWriteOkToWriteOkToCORRUPTED_CORRUPTED_CORRUPTED_'
# victimBuffer size=30, contents: b'CORRUPTED_CORRUPTED_CORRUPTED_'
#
# Note that shortStringBuffer invaded the victimBuffer since the
# string being written was bigger than the shortStringBuffer.
#
# Since no bounds checks were performed, the adjacent memory got
# overwritten and both buffers are now corrupted.
#
# We also have a memory leak of the final block in the memory
# 'oNotWriteHere_DoNotWriteHere_DoNotWriteHere_\x00\x00', caused
# by the null terminator written at the middle of the victimBuffer.
```

如果发现分段冲突，请务必等待 Cppyy 提供的堆栈跟踪 并尝试找到问题的根本原因。如果您有多个内核，则 堆栈跟踪将对应于 Cppyy 正在执行的线程数。为了限制它们， 定义环境变量 OPENBLAS_NUM_THREADS=1。

### 运营商

由于 ns-3 使用的实现样式，Cppyy 可能无法映射C++运算符。 对于基本类型时间，会发生这种情况。为了提供预期的行为，我们 在设置 ns-3 绑定期间从 Python 端重新定义这些运算符 模块（ns-3-dev/bindings/python/ns__init__.py）。


```python
# Redefine Time operators
cppyy.cppdef("""
    using namespace ns3;
    bool Time_ge(Time& a, Time& b){ return a >= b;}
    bool Time_eq(Time& a, Time& b){ return a == b;}
    bool Time_ne(Time& a, Time& b){ return a != b;}
    bool Time_le(Time& a, Time& b){ return a <= b;}
    bool Time_gt(Time& a, Time& b){ return a > b;}
    bool Time_lt(Time& a, Time& b){ return a < b;}
""")
cppyy.gbl.ns3.Time.__ge__ = cppyy.gbl.Time_ge
cppyy.gbl.ns3.Time.__eq__ = cppyy.gbl.Time_eq
cppyy.gbl.ns3.Time.__ne__ = cppyy.gbl.Time_ne
cppyy.gbl.ns3.Time.__le__ = cppyy.gbl.Time_le
cppyy.gbl.ns3.Time.__gt__ = cppyy.gbl.Time_gt
cppyy.gbl.ns3.Time.__lt__ = cppyy.gbl.Time_lt
```

ns-3 使用的另一个运算符是运算符 Address（），用于 将不同类型的地址转换为通用类型的地址。 Cppyy 不支持此功能，需要显式转换。


```python
# Explicitly convert the InetSocketAddress to Address using InetSocketAddress.ConvertTo()
sink.Bind(ns.network.InetSocketAddress(ns.network.Ipv4Address.GetAny(), 80).ConvertTo())
```

如果有足够的时间、耐心和专业知识，大多数缺少的 API 都可以打包，如果提交错误报告，则可能会打包。 但是，不要提交错误报告说“绑定不完整”，因为该项目没有维护者来维护每个 API。

### 描图

Python 尚未正确支持基于回调的跟踪，因为需要提供新的 ns-3 API 才能支持它。

通过普通 API 支持 Pcap 文件写入。

ASCII 跟踪通过转换为 Python 的普通 C++ API 提供支持。 但是，ASCII 跟踪需要创建 ostream 对象才能传递到 ASCII 跟踪方法中。 在 Python 中，C++ std：：ofstream 已被最小化包装以允许这样做。例如：


```python
ascii = ns.ofstream("wifi-ap.tr") # create the file
ns.YansWifiPhyHelper.EnableAsciiAll(ascii)
ns.Simulator.Run()
ns.Simulator.Destroy()
ascii.close() # close the file
```

有一个警告：在 ns-3 仍在使用文件对象时，不得允许对其进行垃圾回收。 这意味着不能允许上面的“ascii”变量超出范围，否则程序将崩溃。

### 使用python 绑定

#### 概述

python 绑定生成到“ns”命名空间中。例子：


```python
from ns import ns
n1 = ns.network.Node()
```


```python
from ns import*
n1 = ns.network.Node()
```

探索绑定的最佳方法是查看各种示例 NS-3 中提供的程序;一些C++示例具有相应的Python 例。Python 绑定没有结构化文档 就像 C++ API 有 Doxygen，但可以咨询 Doxygen 了解C++ API 的工作原理。
