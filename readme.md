### ��¼
��localhost:8080/login����post����������Ϊjson��ʽ������username��password�ֶΣ����磺
```json
{
	"username": "admin",
	"password": "admin"
}
```
����json��ʽ��token�����磺
```json
{
	"token":"eyJhbGci..."
}
```
### ��ȡ������Ϣ
��localhost:8080/datalist/��������������ͷ��Authorization���jwt token

### ����������Ϣ
��localhost:8080/add/����post����������ͷ��Authorization���jwt token
���������磺
```json
{
	'App01BasicInfo':{'����id','���ڼ��ʱ��','����ʱ��','���վ���ͨ��','����ʱ��','������','�Ƿ�ԤӦ������'},��BeamBaseplateConcreteCracking��:{'bridge_id','����װ����������羶','ƽ������','ƽ�����_m2_field','�����_m2_field','����','������_m2_field'},
	'BeamBaseplateXCracking':{'bridge_id','����װ�����ѷ�羶','����ܺ�_mm_field','ƽ�����_mm_field','ƽ������','ƽ������_cm_field','����','�����_mm_field','��󳤶�ռ��','ÿ��������','�����ܺ�_cm_field'},
	'BeamBaseplateYCracking':{'bridge_id','����װ������ѷ�羶','����ܺ�_mm_field','ƽ�����_mm_field','ƽ������','ƽ������_cm_field','����','�����_mm_field','��󳤶�ռ��','�����ܺ�_cm_field'},
	'BeamSteelCorrosion':{'bridge_id','����ֽ���ʴ�羶','ƽ������','ƽ������_m_field','����','��󳤶�_m_field','�����ܺ�_m_field'},
	'BeamWebplateConcreteCracking':{'bridge_id','���帹�����������羶','ƽ������','ƽ�����_m2_field','�����_m2_field','����','������_m2_field'},
	'BeamWebplateZCracking':{'bridge_id','���帹�������ѷ�羶','����ܺ�_mm_field','ƽ�����_mm_field','ƽ������','ƽ������_cm_field','����','�����_mm_field','��󳤶�ռ��','�����ܺ�_cm_field'},
	'BeamWingplateXCracking':{'bridge_id','�����������ѷ�羶','����ܺ�_mm_field','ƽ�����_mm_field','ƽ������','ƽ������_cm_field','ƽ�����','����','�����_mm_field','��󳤶�_cm_field','�����ܺ�_cm_field'},
	'BearingCracking':{'bridge_id','֧�����ѿ羶','����ܺ�_mm_field','ƽ�����_mm_field','ƽ������','ƽ������_cm_field','����','�����_mm_field','��󳤶�_cm_field','�����ܺ�_cm_field'},
	'BearingDeformation':{'bridge_id','֧�����ο羶','ƽ������','����'},
	'BearingHanging':{'bridge_id','֧���ѿտ羶','ƽ������','����'},
	'BridgeGrading':{'bridge_id','�����ȼ�'},
	'ConcreteBreakage':{'bridge_id','������������ѿ羶','ƽ������','ƽ�����_m2_field','�����_m2_field','����','������_m2_field'},
	'PierCracking':{'bridge_id','��̨�ѷ�羶','����ܺ�_m_field','ƽ�����_m_field','ƽ������','ƽ������_cm_field','����','�����_m_field','��󳤶�_cm_field','�����ܺ�_cm_field'},
	'PierSteelCorrosion':{'bridge_id','��̨�ֽʴ�羶','ƽ������','ƽ������_m_field','����','��󳤶�_m_field','�����ܺ�_m_field'}
}
```