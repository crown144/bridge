### 登录
向localhost:8080/login发送post请求，请求体为json格式，包含username和password字段，例如：
```json
{
	"username": "admin",
	"password": "admin"
}
```
返回json格式的token，例如：
```json
{
	"token":"eyJhbGci..."
}
```
### 获取桥梁信息
向localhost:8080/datalist/发送请求，在请求头里Authorization里加jwt token

### 新增桥梁信息
向localhost:8080/add_datalist/发送post请求，在请求头里Authorization里加jwt token
请求体包含15个表及其所有属性，没有的值传null
例如：
```json
{
	"App01BasicInfo":{"桥梁id","定期检查时间","工作时间","年日均交通量","建成时间","上下行","是否预应力桥梁"},
	"BeamBaseplateConcreteCracking":{"bridge_id","梁体底板混凝土破损跨径","平均数量","平均面积_m2_field","总面积_m2_field","数量","最大面积_m2_field"},
	"BeamBaseplateXCracking":{"bridge_id","梁体底板横向裂缝跨径","宽度总和_mm_field","平均宽度_mm_field","平均数量","平均长度_cm_field","数量","最大宽度_mm_field","最大长度占比","每延米数量","长度总和_cm_field"},
	"BeamBaseplateYCracking":{"bridge_id","梁体底板纵向裂缝跨径","宽度总和_mm_field","平均宽度_mm_field","平均数量","平均长度_cm_field","数量","最大宽度_mm_field","最大长度占比","长度总和_cm_field"},
	"BeamSteelCorrosion":{"bridge_id","梁体钢筋锈蚀跨径","平均数量","平均长度_m_field","数量","最大长度_m_field","长度总和_m_field"},
	"BeamWebplateConcreteCracking":{"bridge_id","梁体腹板混凝土破损跨径","平均数量","平均面积_m2_field","总面积_m2_field","数量","最大面积_m2_field"},
	"BeamWebplateZCracking":{"bridge_id","梁体腹板竖向裂缝跨径","宽度总和_mm_field","平均宽度_mm_field","平均数量","平均长度_cm_field","数量","最大宽度_mm_field","最大长度占比","长度总和_cm_field"},
	"BeamWingplateXCracking":{"bridge_id","梁体翼板横向裂缝跨径","宽度总和_mm_field","平均宽度_mm_field","平均数量","平均长度_cm_field","平均间距","数量","最大宽度_mm_field","最大长度_cm_field","长度总和_cm_field"},
	"BearingCracking":{"bridge_id","支座开裂跨径","宽度总和_mm_field","平均宽度_mm_field","平均数量","平均长度_cm_field","数量","最大宽度_mm_field","最大长度_cm_field","长度总和_cm_field"},
	"BearingDeformation":{"bridge_id","支座变形跨径","平均数量","数量"},
	"BearingHanging":{"bridge_id","支座脱空跨径","平均数量","数量"},
	"BridgeGrading":{"bridge_id","桥梁等级"},
	"ConcreteBreakage":{"bridge_id","缩缝混凝土开裂跨径","平均数量","平均面积_m2_field","总面积_m2_field","数量","最大面积_m2_field"},
	"PierCracking":{"bridge_id","墩台裂缝跨径","宽度总和_m_field","平均宽度_m_field","平均数量","平均长度_cm_field","数量","最大宽度_m_field","最大长度_cm_field","长度总和_cm_field"},
	"PierSteelCorrosion":{"bridge_id","墩台钢筋腐蚀跨径","平均数量","平均长度_m_field","数量","最大长度_m_field","长度总和_m_field"}
}
```

### 修改桥梁信息
向localhost:8080/update_datalist/发送post请求，在请求头里Authorization里加jwt token
body示例如下:
```
{
    "bridge_id": "xxx",
	"要修改的表名": {
		"要修改的字段1": "修改后的值",
		"要修改的字段2": "修改后的值",
		...
	}
}
```


### 删除桥梁信息
向localhost:8080/delete_datalist/发送post请求，在请求头里Authorization里加jwt token
body示例如下:
```
{
	"bridge_id": "xxx"
}
```



### 桥梁评估
向localhost:8080/assess/发送post请求
请求体为json,示例见algorithm文件夹下的test.json,
注意：没有的值默认先传0，要求必须有424个字段,不需要id列