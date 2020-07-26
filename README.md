# 朙月拼音·原生简化字

配方： ℞ **ayaka14732/rime-luna-pinyin-simp-native**

rime 朙月拼音输入方案，原生简化字版本

## 特性

本方案的词库使用简化字，可以避免运行时一繁对多简造成的转换错误：

- [x] 徵羽摩柯 ↛ 征羽摩柯
- [x] 复投 ↛ 覆投

本方案预先将朙月拼音原始词库转换为简化字，转换使用的代码见 [`build`](https://github.com/ayaka14732/rime-luna-pinyin-simp-native/tree/build) 分支。

转换使用 OpenCC 程序库，如果发现转换错误，可以直接 patch 转换代码，也可以向 OpenCC 报告错误。

## 用法

拼音字母 ü 用 `v` 键输入。

本方案不支持输入声调。如有需要，请用 [地球拼音](https://github.com/rime/rime-terra-pinyin)。

## 安装

本方案依赖简化字八股文 [rime/rime-essay-simp](https://github.com/rime/rime-essay-simp)。

使用 plum 安装：

```sh
bash rime-install essay-simp ayaka14732/rime-luna-pinyin-simp-native
```

授权条款：见 [LICENSE](LICENSE)
