任务：
补全导出与 iOS 接口协议部分，使算法输出后续可以直接接入 iOS App。

请完成：
1. 在 `ml/training/export_coreml.py` 中补全或改进导出逻辑
2. 明确模型输入输出形状假设
3. 在 `ml/postprocess/` 中确保输出可序列化为 iOS 友好的结构
4. 更新 `docs/ios_integration_contract.md`
5. 更新 `ios_contract/hold_output_schema.json`
6. 如有必要，新增 `ios_contract/example_prediction.json`

约束：
- 以 iOS 端易用性为先
- 默认输出 normalized contour points
- 文档必须足够让 iOS 工程师理解如何接入

输出要求：
- 导出方案说明
- 输出 schema 说明
- 对 iOS 接入方的注意事项
