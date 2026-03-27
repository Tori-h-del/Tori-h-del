from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    page_data = {
        "project_name": "译愿桥（暂定）",
        "tagline": "翻译兼职 + 志愿时长：学生拿钱的同时还能拿官方志愿时长",
        "value_statement": "这是其他平台给不了的核心价值。",
        "core_values": [
            "学生端零抽成：学生完成任务后全额拿到约定报酬",
            "企业端规范收费：平台仅向企业收取服务费",
            "官方志愿时长累计：任务完成后自动同步志愿时长记录",
            "资金托管结算：降低拖欠风险，保障交付与回款",
        ],
        "student_features": [
            "实名认证 + 语言能力标签（英/日/韩/小语种）",
            "任务大厅：按语种、领域、时限筛选",
            "报价透明：学生清楚企业预算与自身实得",
            "志愿证明导出：支持评优、奖学金、入党材料",
        ],
        "enterprise_features": [
            "快速发布翻译需求（文档/字幕/口译）",
            "按语种与专业方向匹配学生译员",
            "进度可视化 + 节点验收",
            "统一结算与发票管理",
        ],
        "mvp_modules": [
            "用户系统：学生/企业双端注册登录",
            "任务系统：发布、接单、交付、验收",
            "结算系统：托管、放款、服务费计费",
            "志愿系统：时长累计、审核、证明生成",
            "评价系统：双向评分与信用分",
        ],
    }
    return render_template("index.html", data=page_data)


@app.route("/health")
def health():
    return jsonify({"status": "ok", "framework": "flask"})


if __name__ == "__main__":
    app.run(debug=True)
