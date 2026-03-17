# 工程分析（Phase 1）：攀岩岩点识别算法准备

## 1) 当前仓库结构与目标总结

### 总体定位
本仓库当前是**算法模块准备仓库**，重点不在 iOS UI 集成，而是在后续可接入 iOS 的可训练/可评估/可导出算法路径建设。

### 目标能力（当前阶段）
- 数据集识别与适配（`ml/data/` -> `ml/datasets/`）
- 训练与评估入口（`ml/training/`）
- 推理入口（`ml/inference/`）
- 后处理（mask -> contour -> 归一化点）（`ml/postprocess/`）
- Core ML 导出路径（`ml/training/export_coreml.py`）
- iOS 输出协议（`docs/ios_integration_contract.md` + `ios_contract/*.json`）

### 目录现状
- `docs/`：目标、验收、数据规范、iOS 协议文档
- `plans/`：当前执行计划（Phase 1）
- `prompts/`：分步骤 Codex 执行提示
- `ml/`：算法代码骨架
  - `configs/`：baseline 配置（当前为 placeholder）
  - `datasets/`：数据接口与占位 adapter
  - `training/`：train/eval/export 占位入口
  - `inference/`：推理占位入口
  - `postprocess/`：轮廓提取与输出格式（已有可运行基础实现）
  - `tools/`：数据检查脚本（可运行）
- `ios_contract/`：JSON schema 与示例输出

## 2) `ml/data/` 数据检查与格式判断

### 检查结果
当前 `ml/data/` 下仅发现一个文件：`11`（文件内容为字符串 `11\n`），未发现图片、标注、split 目录。

### 结论
- **尚无可用训练数据**。
- 暂时**无法确定真实数据集格式**（COCO / YOLO seg / mask / custom JSON 均无证据）。

### 合理假设（待确认）
1. 该文件可能是占位文件，用于保持目录非空。
2. 后续会补充真实数据到 `ml/data/`。
3. 最可能首选格式是 YOLO segmentation 或 COCO segmentation（与当前“轻量+可导出”目标兼容性较高）。

## 3) 建议 baseline 技术路线

### 推荐主路线（优先）
1. **数据层：优先适配 YOLO segmentation**（如真实数据不是 YOLO，则加转换工具）
2. **模型层：Ultralytics YOLO Seg 轻量模型**（例如 n/s 级别）
3. **训练评估：先跑通训练/验证最小闭环**（mAP、mask 指标 + 失败样本输出）
4. **推理后处理：保留当前 mask->contour 基础模块并增强稳定性**
5. **导出：先 ONNX 再 Core ML（或直接 Ultralytics/CoreMLTools 路径）**
6. **协议：严格按 iOS contract 输出 normalized_contour_points**

### 选择理由
- 与仓库 AGENTS 指南一致：轻量、可导出、模块化。
- 与 iOS 后续集成路径一致：轮廓与归一化点是核心。
- 可以先保证“可运行闭环”，再优化精度与速度。

### 备选路线
- 若数据是 COCO：实现 COCO adapter + 可选转换到 YOLO seg 的工具。
- 若数据是 mask/custom JSON：先统一转换为中间格式（推荐 YOLO seg 或内部统一 JSON）再训练。

## 4) 建议修改/新增文件（文件级）

> 本次仅分析，不做大规模实现；以下为建议清单。

### 文档类
- `docs/dataset_spec.md`：补全真实数据格式、目录、类目、split、脏数据规则
- `README.md`：补充一键跑通命令（inspect/train/eval/predict/export）
- `docs/ios_integration_contract.md`：补充边界条件（空轮廓、异常点、裁剪策略）

### 数据与工具
- `ml/datasets/yolo_seg_adapter.py`（新增）：YOLO segmentation 读取器
- `ml/datasets/coco_seg_adapter.py`（可选新增）：COCO segmentation 读取器
- `ml/tools/convert_coco_to_yolo_seg.py`（可选新增）：转换工具
- `ml/tools/validate_annotations.py`（新增）：标注合法性校验

### 训练/评估/推理
- `ml/configs/baseline.yaml`：替换 placeholder family 为真实模型配置
- `ml/training/train.py`：接入真实训练流程
- `ml/training/eval.py`：接入评估与错误样本导出
- `ml/inference/predict.py`：接入真实模型推理 + 后处理流程
- `ml/training/export_coreml.py`：完善导出参数、输入输出说明、失败提示

### 后处理与输出
- `ml/postprocess/contours.py`：增加闭合检查、最小点数校验、可选排序一致性
- `ml/postprocess/format_output.py`：增加 schema 级字段校验/兼容处理
- `ios_contract/hold_output_schema.json`：与实际输出字段完全对齐
- `ios_contract/example_prediction.json`：增加 2~3 个典型 case（正常/小目标/低置信）

## 5) 分阶段实施计划（建议）

### Phase A：数据落地与格式确认（1~2 天）
- 放入最小可运行样本数据（train/val）
- 运行 inspect + annotation validate
- 更新 `docs/dataset_spec.md`
- 决策是否需要格式转换

**产出**：明确数据格式与 adapter 方案。

### Phase B：训练/评估最小闭环（2~4 天）
- 完成真实 dataset adapter
- 打通 baseline train/eval 脚本
- 产出最小指标与失败样本目录

**产出**：可训练可评估 pipeline。

### Phase C：推理与后处理稳定化（1~2 天）
- 推理脚本接入真实模型
- 完善 contour 提取（去噪、简化、闭合保障）
- 输出对齐 iOS contract

**产出**：可消费 JSON 预测结果。

### Phase D：导出与契约冻结（1~2 天）
- 完成 Core ML 导出脚本（含输入输出形状文档）
- 更新 schema 与示例
- 记录导出限制与兼容性

**产出**：可交付给 iOS 的模型与协议文档。

### Phase E：验收与风险回归（1 天）
- 对照 `docs/acceptance_criteria.md` 做 checklist
- 补齐 README 运行命令
- 记录 open issues

**产出**：Phase 1 可交付包。

## 风险与待确认项

### 高风险
1. 当前无真实数据，无法验证任何模型/评估结论。
2. 真实标注质量未知（多边形合法性、漏标、重叠规则）。
3. Core ML 导出能力强依赖最终模型框架与算子支持。

### 待确认
1. 类别是否只有 `hold`（是否包含 volume/wall）。
2. 是否需要颜色元数据用于后续业务逻辑。
3. iOS 端是否需要固定点数轮廓（例如采样成 N 点）。
4. 低置信度目标是否返回（阈值策略）。

## 建议的下一步（最小动作）
1. 先在 `ml/data/` 放入 20~50 张带标注样本。
2. 立即更新 `docs/dataset_spec.md`（真实格式第一版）。
3. 选定 baseline（推荐 YOLO seg）并开始适配 `ml/datasets/`。
