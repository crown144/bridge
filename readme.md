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
向localhost:8080/add/发送post请求，在请求头里Authorization里加jwt token
请求体例如：
```json
{
	'App01BasicInfo':{'桥梁id','定期检查时间','工作时间','年日均交通量','建成时间','上下行','是否预应力桥梁'},‘BeamBaseplateConcreteCracking’:{'bridge_id','梁体底板混凝土破损跨径','平均数量','平均面积_m2_field','总面积_m2_field','数量','最大面积_m2_field'},
	'BeamBaseplateXCracking':{'bridge_id','梁体底板横向裂缝跨径','宽度总和_mm_field','平均宽度_mm_field','平均数量','平均长度_cm_field','数量','最大宽度_mm_field','最大长度占比','每延米数量','长度总和_cm_field'},
	'BeamBaseplateYCracking':{'bridge_id','梁体底板纵向裂缝跨径','宽度总和_mm_field','平均宽度_mm_field','平均数量','平均长度_cm_field','数量','最大宽度_mm_field','最大长度占比','长度总和_cm_field'},
	'BeamSteelCorrosion':{'bridge_id','梁体钢筋锈蚀跨径','平均数量','平均长度_m_field','数量','最大长度_m_field','长度总和_m_field'},
	'BeamWebplateConcreteCracking':{'bridge_id','梁体腹板混凝土破损跨径','平均数量','平均面积_m2_field','总面积_m2_field','数量','最大面积_m2_field'},
	'BeamWebplateZCracking':{'bridge_id','梁体腹板竖向裂缝跨径','宽度总和_mm_field','平均宽度_mm_field','平均数量','平均长度_cm_field','数量','最大宽度_mm_field','最大长度占比','长度总和_cm_field'},
	'BeamWingplateXCracking':{'bridge_id','梁体翼板横向裂缝跨径','宽度总和_mm_field','平均宽度_mm_field','平均数量','平均长度_cm_field','平均间距','数量','最大宽度_mm_field','最大长度_cm_field','长度总和_cm_field'},
	'BearingCracking':{'bridge_id','支座开裂跨径','宽度总和_mm_field','平均宽度_mm_field','平均数量','平均长度_cm_field','数量','最大宽度_mm_field','最大长度_cm_field','长度总和_cm_field'},
	'BearingDeformation':{'bridge_id','支座变形跨径','平均数量','数量'},
	'BearingHanging':{'bridge_id','支座脱空跨径','平均数量','数量'},
	'BridgeGrading':{'bridge_id','桥梁等级'},
	'ConcreteBreakage':{'bridge_id','缩缝混凝土开裂跨径','平均数量','平均面积_m2_field','总面积_m2_field','数量','最大面积_m2_field'},
	'PierCracking':{'bridge_id','墩台裂缝跨径','宽度总和_m_field','平均宽度_m_field','平均数量','平均长度_cm_field','数量','最大宽度_m_field','最大长度_cm_field','长度总和_cm_field'},
	'PierSteelCorrosion':{'bridge_id','墩台钢筋腐蚀跨径','平均数量','平均长度_m_field','数量','最大长度_m_field','长度总和_m_field'}
}
```