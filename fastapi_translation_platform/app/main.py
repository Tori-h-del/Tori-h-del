from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="大学生翻译平台（初步版）",
    description="面向大学生与企业的翻译兼职撮合平台初步框架",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    """首页：展示平台定位与核心模块。"""
    page_data = {
        "project_name": "XX 译栈",
        "founder": "覃勇茹",
        "start_time": "2026 年 3 月",
        "version": "V1.0",
        "slogan": "做翻译兼职，钱全拿，还能拿官方志愿时长",
        "pain_points": [
            {
                "pain": "中介抽成高（50%-70%）",
                "solution": "平台不抽学生钱，仅向企业收取 15%-20% 服务费",
            },
            {
                "pain": "拖欠工资",
                "solution": "资金托管，任务完成后自动结算",
            },
            {
                "pain": "无保障",
                "solution": "平台配套意外保险",
            },
            {
                "pain": "无成长积累",
                "solution": "任务累计官方志愿时长，用于评优/入党/奖学金",
            },
            {
                "pain": "信息不透明",
                "solution": "学生知道企业出价，企业知道学生实得",
            },
        ],
        "student_users": [
            "在校大学生，韩语/日语/英语及小语种优先",
            "希望通过兼职赚钱，同时积累志愿时长",
            "被中介坑过，想要更公平的平台",
        ],
        "enterprise_users": [
            "翻译公司、跨境电商、留学机构、外企",
            "有小语种翻译需求",
            "愿意为“规范+高效”支付服务费",
        ],
        "revenue": [
            "企业服务费：任务金额 × 15%-20%（核心收入）",
            "加急匹配费：50-100 元/次（24 小时内需求）",
        ],
        "features": [
            "学生实名认证与语言能力标签",
            "任务大厅与智能匹配",
            "托管结算与评价体系",
            "志愿时长自动累计与证明导出",
        ],
    }
    return templates.TemplateResponse("index.html", {"request": request, "data": page_data})


@app.get("/health")
def health_check():
    return {"status": "ok"}
