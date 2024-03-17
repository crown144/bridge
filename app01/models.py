from django.db import models


class App01BasicInfo(models.Model):
    桥梁id = models.CharField(primary_key=True, max_length=255)
    定期检查时间 = models.TextField(blank=True, null=True)  # This field type is a guess.
    工作时间 = models.IntegerField(blank=True, null=True)
    年日均交通量 = models.IntegerField(blank=True, null=True)
    建成时间 = models.TextField(blank=True, null=True)  # This field type is a guess.
    上下行 = models.IntegerField(blank=True, null=True)
    是否预应力桥梁 = models.IntegerField(blank=True, null=True)
    上传用户 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app01_basic_info'


class user_info(models.Model):
    Permission_CHOICES = (
        ('A', 'Admin'),
        ('C', 'Client'),
        ('E', 'Enterprise'),
    )
    username = models.CharField(verbose_name='用户名',max_length=16)
    password = models.CharField(verbose_name='密码',max_length=64)
    enterprise_name = models.CharField(verbose_name='企业名',max_length=64,blank=True,null=True)
    permission = models.CharField(max_length=1, choices=Permission_CHOICES,default='C')
    def __str__(self):
        return self.username


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BeamBaseplateConcreteCracking(models.Model):
    bridge_id = models.CharField(primary_key=True, max_length=255)
    梁体底板混凝土破损跨径 = models.IntegerField(blank=True, null=True)
    平均数量 = models.FloatField(blank=True, null=True)
    平均面积_m2_field = models.FloatField(db_column='平均面积(m2)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    总面积_m2_field = models.FloatField(db_column='总面积(m2)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    数量 = models.IntegerField(blank=True, null=True)
    最大面积_m2_field = models.FloatField(db_column='最大面积(m2)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'beam baseplate concrete cracking'


class BeamBaseplateXCracking(models.Model):
    bridge_id = models.CharField(primary_key=True, max_length=255)
    梁体底板横向裂缝跨径 = models.IntegerField(blank=True, null=True)
    宽度总和_mm_field = models.FloatField(db_column='宽度总和(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    平均宽度_mm_field = models.FloatField(db_column='平均宽度(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    平均数量 = models.FloatField(blank=True, null=True)
    平均长度_cm_field = models.FloatField(db_column='平均长度(cm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    数量 = models.IntegerField(blank=True, null=True)
    最大宽度_mm_field = models.FloatField(db_column='最大宽度(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    最大长度占比 = models.FloatField(blank=True, null=True)
    每延米数量 = models.FloatField(blank=True, null=True)
    长度总和_cm_field = models.FloatField(db_column='长度总和(cm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'beam baseplate x cracking'


class BeamBaseplateYCracking(models.Model):
    bridge_id = models.CharField(primary_key=True, max_length=255)
    梁体底板纵向裂缝跨径 = models.IntegerField(blank=True, null=True)
    宽度总和_mm_field = models.FloatField(db_column='宽度总和(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    平均宽度_mm_field = models.FloatField(db_column='平均宽度(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    平均数量 = models.FloatField(blank=True, null=True)
    平均长度_cm_field = models.FloatField(db_column='平均长度(cm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    数量 = models.IntegerField(blank=True, null=True)
    最大宽度_mm_field = models.FloatField(db_column='最大宽度(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    最大长度占比 = models.FloatField(blank=True, null=True)
    长度总和_cm_field = models.FloatField(db_column='长度总和(cm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'beam baseplate y cracking'


class BeamSteelCorrosion(models.Model):
    bridge_id = models.CharField(primary_key=True, max_length=255)
    梁体钢筋锈蚀跨径 = models.IntegerField(blank=True, null=True)
    平均数量 = models.FloatField(blank=True, null=True)
    平均长度_m_field = models.FloatField(db_column='平均长度(m)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    数量 = models.IntegerField(blank=True, null=True)
    最大长度_m_field = models.FloatField(db_column='最大长度(m)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    长度总和_m_field = models.FloatField(db_column='长度总和(m)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'beam steel corrosion'


class BeamWebplateConcreteCracking(models.Model):
    bridge_id = models.CharField(max_length=255, blank=True, null=True)
    梁体腹板混凝土破损跨径 = models.IntegerField(blank=True, null=True)
    平均数量 = models.FloatField(blank=True, null=True)
    平均面积_m2_field = models.FloatField(db_column='平均面积(m2)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    总面积_m2_field = models.FloatField(db_column='总面积(m2)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    数量 = models.IntegerField(blank=True, null=True)
    最大面积_m2_field = models.FloatField(db_column='最大面积(m2)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'beam webplate concrete cracking'


class BeamWebplateZCracking(models.Model):
    bridge_id = models.CharField(primary_key=True, max_length=255)
    梁体腹板竖向裂缝跨径 = models.IntegerField(blank=True, null=True)
    宽度总和_mm_field = models.FloatField(db_column='宽度总和(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    平均宽度_mm_field = models.FloatField(db_column='平均宽度(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    平均数量 = models.FloatField(blank=True, null=True)
    平均长度_cm_field = models.FloatField(db_column='平均长度(cm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    数量 = models.IntegerField(blank=True, null=True)
    最大宽度_mm_field = models.FloatField(db_column='最大宽度(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    最大长度占比 = models.FloatField(blank=True, null=True)
    长度总和_cm_field = models.FloatField(db_column='长度总和(cm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'beam webplate z cracking'


class BeamWingplateXCracking(models.Model):
    bridge_id = models.CharField(primary_key=True, max_length=255)
    梁体翼板横向裂缝跨径 = models.IntegerField(blank=True, null=True)
    宽度总和_mm_field = models.FloatField(db_column='宽度总和(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    平均宽度_mm_field = models.FloatField(db_column='平均宽度(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    平均数量 = models.FloatField(blank=True, null=True)
    平均长度_cm_field = models.FloatField(db_column='平均长度(cm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    平均间距 = models.FloatField(blank=True, null=True)
    数量 = models.IntegerField(blank=True, null=True)
    最大宽度_mm_field = models.FloatField(db_column='最大宽度(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    最大长度_cm_field = models.FloatField(db_column='最大长度(cm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    长度总和_cm_field = models.FloatField(db_column='长度总和(cm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'beam wingplate x cracking'


class BearingCracking(models.Model):
    bridge_id = models.CharField(primary_key=True, max_length=255)
    支座开裂跨径 = models.IntegerField(blank=True, null=True)
    宽度总和_mm_field = models.FloatField(db_column='宽度总和(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    平均宽度_mm_field = models.FloatField(db_column='平均宽度(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    平均数量 = models.FloatField(blank=True, null=True)
    平均长度_cm_field = models.FloatField(db_column='平均长度(cm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    数量 = models.IntegerField(blank=True, null=True)
    最大宽度_mm_field = models.FloatField(db_column='最大宽度(mm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    最大长度_cm_field = models.FloatField(db_column='最大长度(cm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    长度总和_cm_field = models.FloatField(db_column='长度总和(cm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'bearing cracking'


class BearingDeformation(models.Model):
    bridge_id = models.CharField(primary_key=True, max_length=255)
    支座变形跨径 = models.IntegerField(blank=True, null=True)
    平均数量 = models.FloatField(blank=True, null=True)
    数量 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bearing deformation'


class BearingHanging(models.Model):
    bridge_id = models.CharField(primary_key=True, max_length=255)
    支座脱空跨径 = models.IntegerField(blank=True, null=True)
    平均数量 = models.FloatField(blank=True, null=True)
    数量 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bearing hanging'


class BridgeGrading(models.Model):
    桥梁id = models.CharField(primary_key=True, max_length=255)
    桥梁评级 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bridge grading'


class ConcreteBreakage(models.Model):
    bridge_id = models.CharField(db_column='bridge id', primary_key=True, max_length=255)  # Field renamed to remove unsuitable characters.
    缩缝混凝土开裂跨径 = models.IntegerField(blank=True, null=True)
    平均数量 = models.FloatField(blank=True, null=True)
    平均面积_m2_field = models.FloatField(db_column='平均面积(m2)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    总面积_m2_field = models.FloatField(db_column='总面积(m2)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    数量 = models.IntegerField(blank=True, null=True)
    最大面积_m2_field = models.FloatField(db_column='最大面积(m2)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'concrete breakage'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PierCracking(models.Model):
    bridge_id = models.CharField(primary_key=True, max_length=255)
    墩台裂缝跨径 = models.IntegerField(blank=True, null=True)
    宽度总和_m_field = models.FloatField(db_column='宽度总和(m)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    平均宽度_m_field = models.FloatField(db_column='平均宽度(m)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    平均数量 = models.FloatField(blank=True, null=True)
    平均长度_cm_field = models.FloatField(db_column='平均长度(cm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    数量 = models.IntegerField(blank=True, null=True)
    最大宽度_m_field = models.FloatField(db_column='最大宽度(m)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    最大长度_cm_field = models.FloatField(db_column='最大长度(cm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    长度总和_cm_field = models.FloatField(db_column='长度总和(cm)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'pier cracking'


class PierSteelCorrosion(models.Model):
    bridge_id = models.CharField(primary_key=True, max_length=255)
    墩台钢筋腐蚀跨径 = models.IntegerField(blank=True, null=True)
    平均数量 = models.FloatField(blank=True, null=True)
    平均长度_m_field = models.FloatField(db_column='平均长度(m)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    数量 = models.IntegerField(blank=True, null=True)
    最大长度_m_field = models.FloatField(db_column='最大长度(m)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    长度总和_m_field = models.FloatField(db_column='长度总和(m)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'pier steel corrosion'
