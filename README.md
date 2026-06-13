# Research Knowledge Base Skill

一个面向科研人员的 Codex Skill，用于构建和维护 **Zotero + Obsidian + Codex** 文献知识库。

它将文献管理、深度阅读和知识综合分开：

- **Zotero** 保存文献条目、PDF、元数据、批注和阅读过程中的实时问题。
- **Obsidian** 保存经过核对的文献笔记、项目证据、主题知识、方法概念和综合判断。
- **Codex** 负责初始化结构、读取文献、核对实时问答、写入笔记并维护知识连接。

> **English:** A reusable Codex Skill for building and maintaining a research literature knowledge base with Zotero, Obsidian, and Codex. It supports deep reading of original studies and reviews, project evidence maps, topic MOCs, method notes, synthesis, and source-verified integration of real-time Zotero questions.

## 核心特点

- 不绑定具体疾病、学科或研究项目。
- 每篇文献只保留一篇正式精读笔记，避免多个项目重复总结。
- 区分原始研究和综述，使用不同深度阅读模板。
- 原始研究重点展开方法与 Figure/Result 逻辑。
- 综述重点展开领域框架、证据地图、趋势争议和后续原始文献。
- 新建 Project 时优先复用已有文献，不要求重读全部文献。
- 支持 Zotero `阅读追问_QA` child note。
- 将 PapersGPT 等工具产生的实时回答视为临时答案，回到原文核对后再入库。
- 提供安全的初始化脚本，不覆盖现有文件。
- Skill 本身不要求 OpenAI API key。

## 知识库结构

```text
My Research Knowledge Base
├── 01_Literature
├── 02_Projects
├── 03_Topics
├── 04_Methods_Concepts
├── 05_Synthesis
└── 90_Templates
```

| 文件夹 | 用途 |
|---|---|
| `01_Literature` | 每篇文献唯一的正式精读笔记 |
| `02_Projects` | 围绕具体课题组织证据、缺口和下一步 |
| `03_Topics` | 跨文献、跨项目的主题页和 MOC |
| `04_Methods_Concepts` | 方法、数据集、marker、通路、模型和分析流程 |
| `05_Synthesis` | 多篇文献整合后的判断、假说和写作素材 |
| `90_Templates` | 原始研究、综述、Project、Topic、Method、Synthesis 和实时追问模板 |

## 安装 Skill

### 方法一：让 Codex 安装

把 GitHub 仓库地址发给 Codex：

```text
请从这个 GitHub 仓库安装 Codex Skill：
https://github.com/tianliang-liu/research-knowledge-base-skill

Skill 路径是：
skill/research-knowledge-base
```

### 方法二：手动安装

```bash
git clone https://github.com/tianliang-liu/research-knowledge-base-skill.git
mkdir -p ~/.codex/skills
cp -R research-knowledge-base-skill/skill/research-knowledge-base \
  ~/.codex/skills/research-knowledge-base
```

重新打开 Codex 会话后，可以通过 `$research-knowledge-base` 显式调用。

## 初始化知识库

### 让 Codex 初始化

```text
请使用 $research-knowledge-base，在我的 Obsidian vault 中建立一个独立科研知识库。

知识库名称：
主要研究方向：
长期核心问题：
当前项目：
重点样本：
重点技术：
Zotero collections：
```

一个完整的虚构示例见：

[examples/initialization-profile.example.md](examples/initialization-profile.example.md)

### 直接运行初始化脚本

```bash
python3 skill/research-knowledge-base/scripts/init_knowledge_base.py \
  --destination "/path/to/your/obsidian-vault" \
  --name "My Research Knowledge Base"
```

向已有知识库补充缺少的模板：

```bash
python3 skill/research-knowledge-base/scripts/init_knowledge_base.py \
  --destination "/path/to/your/obsidian-vault" \
  --name "My Research Knowledge Base" \
  --merge
```

`--merge` 只复制缺失文件，不覆盖已有内容。

初始化后，在 Obsidian 中设置：

```text
Settings
→ Core plugins
→ Templates
→ Template folder location
→ My Research Knowledge Base/90_Templates
```

## 精读文献

### 原始研究

```text
请使用 $research-knowledge-base 处理 Zotero 文献“<标题>”。

请读取全文，按原始研究模板完成深度精读。方法和每个主要 Figure/Result 必须详细展开；完成后把高价值内容沉淀到相关 Project、Topic、Method 或 Synthesis 页面。
```

### 综述

```text
请使用 $research-knowledge-base 处理 Zotero 综述“<标题>”。

请还原作者的领域框架，区分证据等级，逐主题拆解，整理关键原始文献、方法、数据集、药物或机制，并说明对当前项目的影响。
```

支持的输入包括：

- Zotero 标题或 item key
- 本地 PDF
- DOI
- PMID / PMCID
- 文章网页链接

如果只能访问摘要，Codex 应明确标记为摘要级分析，而不能声称完成全文精读。

## Zotero 实时提问

建议在每篇 Zotero 文献条目下创建一个 child note：

```text
阅读追问_QA
```

阅读 PDF 时记录：

```markdown
## Q001

- 原文位置：
- 原文摘录：
- 我的实时问题：
- AI 实时回答：
- 我自己的理解：
- 需要 Codex 核对：是
```

之后请求：

```text
请使用 $research-knowledge-base 处理这篇 Zotero 文献。
它下面有一个“阅读追问_QA”子笔记。请逐条回到 PDF 核对临时 AI 回答，纠错并把经过验证的解释整合进正式文献笔记。
```

PapersGPT、本地模型、MCP 或其他聊天工具都可以用于即时回答，但这些回答不能直接作为论文证据。

## 新建 Project

```text
请使用 $research-knowledge-base 新建项目“<项目名称>”。

请先搜索 01_Literature 中已有文献，按核心证据、背景、方法和外围相关性分类，建立证据地图和缺口清单。不要要求我重新阅读所有旧文献。
```

Project 页面是动态研究地图，不是第二套文献摘要。

## 定期维护

```text
请使用 $research-knowledge-base 检查我的知识库：

1. 找出 reading 或 summarized 状态的文献；
2. 找出尚未沉淀到上层页面的内容；
3. 更新 Project 证据缺口；
4. 检查未解决的实时追问和失效 wikilink；
5. 推荐下一批最值得精读的文献。
```

## 是否需要 API

这个 Skill 和初始化脚本本身不调用模型 API。

- Codex 是否能直接读取 Zotero，取决于当前环境是否提供 Zotero 本地接口、插件、MCP 或文件访问能力。
- PapersGPT 在 Zotero 内调用远程模型时，可能需要相应模型服务的 API key。
- 本地模型可以减少文献内容向第三方传输，但不能替代原文核对。
- MCP 是客户端访问 Zotero 或本地文档的连接方式，不等同于模型服务，也不自动保证答案准确。

## 隐私

- 不要把患者身份信息、未公开数据或敏感项目材料发送给未获批准的远程模型。
- 发布或分享知识库模板前，扫描绝对路径、账号、邮件、项目名称和私有文献内容。
- AI 生成的实时答案必须标记为临时答案，并在正式入库前验证。

## 仓库结构

```text
skill/research-knowledge-base/
├── SKILL.md
├── agents/openai.yaml
├── scripts/init_knowledge_base.py
├── references/
└── assets/vault-template/
```

## 验证

```bash
python3 -m unittest discover -s tests -v
python3 /path/to/skill-creator/scripts/quick_validate.py \
  skill/research-knowledge-base
```

## License

[MIT License](LICENSE)
