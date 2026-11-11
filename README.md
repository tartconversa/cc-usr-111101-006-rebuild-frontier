# 迟到更正驱动的分区依赖与最小补算

本项目保存公园阅读空间经营数据格式与原始资料读取程序。当前读取器只输出输入类型和条数，不加工业务事实，不修改数据。资料中的标识、数量和金额均为合成值。

## 格式与目录

fixtures 保存输入，src/dag_reader.py 为读取入口，tests 核对读取行为。依赖边从上游指向下游。保留日期与截止日期在 partitions.json。样本动作仅写入输入摘要，不负责调度、恢复或发布。

## 运行命令

Python 3.11 及以上，只使用标准库，无第三方安装步骤。进入项目根目录运行：

    python -m src.dag_reader fixtures/dag.json

编译检查：

    python -m compileall -q src tests

读取测试：

    python -m unittest discover -s tests -v

## 容器方式

    docker build -t rebuild-frontier:local .
    docker run --rm rebuild-frontier:local

容器默认执行读取测试。数据加工输出请写入独立路径，避免覆盖原始资料。
