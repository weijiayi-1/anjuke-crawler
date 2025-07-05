# 安居客二手房爬虫

一个基于Python的安居客二手房数据爬虫项目，专门用于爬取各城市的二手房信息。

## 项目简介

本项目使用Selenium和BeautifulSoup技术栈，自动化爬取安居客网站上的二手房数据，并将数据存储到MySQL数据库中。项目主要针对广西地区的14个城市进行数据采集。

## 功能特性

- 🏠 **多城市数据采集**：支持各个城市的二手房数据爬取
- 📊 **实时数据存储**：爬取过程中实时将数据写入MySQL数据库
- 🔄 **智能分页处理**：自动处理分页逻辑，避免重复数据
- 📈 **房龄分类**：按房龄分类采集（2年内、2-5年）
- 🛡️ **反爬虫策略**：使用Selenium模拟真实浏览器行为

## 项目结构

```
anjukecrawler/
├── config.py      # 配置文件（数据库连接、城市列表）
├── crawler.py     # 爬虫核心逻辑
├── db.py          # 数据库操作类
├── main.py        # 程序入口
├── requirements.txt # 项目依赖
└── README.md      # 项目文档
```

## 数据字段

爬取的二手房数据包含以下字段：

| 字段名 | 描述 | 示例 |
|--------|------|------|
| 标题 | 房源标题 | "精装修三房两厅" |
| 户型 | 房屋户型 | "3室2厅1卫" |
| 面积 | 房屋面积 | "89㎡" |
| 方位 | 房屋朝向 | "南北通透" |
| 楼层 | 楼层信息 | "中层/6层" |
| 时间 | 建造时间 | "2018年建造" |
| 所属小区 | 小区名称 | "阳光花园" |
| 所属区域 | 所在区域 | "青秀区" |
| 总价 | 房屋总价 | "120万" |
| 均价 | 每平米价格 | "13483元/㎡" |
| 房龄 | 房龄分类 | "2年内" 或 "2-5年" |

## 支持的城市

项目支持爬取多个城市的二手房数据，城市列表可在 `config.py` 文件中灵活配置。

### 自定义城市配置

如需添加或修改城市，请编辑 `config.py` 文件中的 `GX_CITIES` 列表：

```python
GX_CITIES = [
    'beijing', 'shanghai', 'guangzhou',  # 示例城市
    'shenzhen', 'hangzhou', 'nanjing',   # 更多城市
    # 添加更多城市...
]
```

**注意**：城市拼音需要与安居客网站URL中的城市标识保持一致。

## 安装与配置

### 1. 环境要求

- Python 3.7+
- MySQL 5.7+
- Chrome浏览器

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 数据库配置

在 `config.py` 文件中配置MySQL数据库连接信息：

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'ershoufang',
    'port': 3306
}
```

### 4. 创建数据库

在MySQL中创建名为 `ershoufang` 的数据库：

```sql
CREATE DATABASE ershoufang CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

## 使用方法

### 运行爬虫

```bash
python main.py
```

程序将自动：
1. 连接到MySQL数据库
2. 创建数据表（如果不存在）
3. 依次爬取所有配置城市的二手房数据
4. 实时将数据存储到数据库中

### 爬取逻辑

- 每个城市爬取2年内和2-5年房龄的房源
- 每个房龄分类最多爬取4页数据
- 自动检测页面结束条件，避免无效爬取
- 爬取间隔3秒，避免对目标网站造成压力

## 注意事项

⚠️ **重要提醒**：

1. **合法使用**：请确保遵守安居客网站的使用条款和robots.txt协议
2. **爬取频率**：建议控制爬取频率，避免对目标网站造成过大压力
3. **数据用途**：爬取的数据仅供学习和研究使用，不得用于商业用途
4. **反爬虫**：网站可能会更新反爬虫机制，需要及时调整代码

## 技术栈

- **Python 3.7+**：主要编程语言
- **Selenium**：浏览器自动化，模拟真实用户行为
- **BeautifulSoup4**：HTML解析和数据提取
- **PyMySQL**：MySQL数据库连接和操作
- **Chrome WebDriver**：浏览器驱动

## 数据库表结构

```sql
CREATE TABLE ershoufang_list (
    id INT AUTO_INCREMENT PRIMARY KEY,
    标题 VARCHAR(255),
    户型 VARCHAR(64),
    面积 VARCHAR(64),
    方位 VARCHAR(64),
    楼层 VARCHAR(64),
    时间 VARCHAR(64),
    所属小区 VARCHAR(255),
    所属区域 VARCHAR(255),
    总价 VARCHAR(64),
    均价 VARCHAR(64),
    房龄 VARCHAR(32)
) CHARACTER SET utf8mb4;
```

## 故障排除

### 常见问题

1. **ChromeDriver错误**
   - 确保已安装Chrome浏览器
   - 下载对应版本的ChromeDriver并添加到PATH

2. **数据库连接失败**
   - 检查MySQL服务是否启动
   - 验证数据库配置信息是否正确
   - 确保数据库用户有足够权限

3. **爬取数据为空**
   - 检查网络连接
   - 验证目标网站是否可访问
   - 确认CSS选择器是否仍然有效

## 许可证

本项目仅供学习和研究使用，请遵守相关法律法规和网站使用条款。

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 更新日志

- **v1.0.0**：初始版本，支持各个城市的二手房数据爬取 
