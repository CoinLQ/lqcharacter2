from rect.models import *
from rect.utils import allocateTasks
from django.db.models import Min, Sum


class GenTask(object):

    @staticmethod
    def gen_cctask_by_plan():
        for stask in Schedule_Task_Statistical.objects.filter(amount_of_cctasks=-1):
            # 未激活说明，第一步的CC阈值没有填写
            if stask.schedule.status == ScheduleStatus.NOT_ACTIVE:
                continue
            # 逐卷创建任务
            for rtask in Reel_Task_Statistical.objects.filter(schedule=stask.schedule).prefetch_related('reel'):
                if rtask.amount_of_cctasks != -1:
                    continue
                count = allocateTasks(stask.schedule, rtask.reel, SliceType.CC)
                rtask.amount_of_cctasks = count
                rtask.save(update_fields=['amount_of_cctasks'])
            # 检查每卷大于-1，开启总计划，更新任务数。
            quertset = Reel_Task_Statistical.objects.filter(schedule=stask.schedule)
            result = quertset.aggregate(Min('amount_of_cctasks'))
            # 只有所有卷都开启任务，计划表的总任务数才更新。
            if result['amount_of_cctasks__min'] != -1:
                count = quertset.aggregate(Sum('amount_of_cctasks'))['amount_of_cctasks__sum']
                stask.amount_of_cctasks = count
                stask.save(update_fields=['amount_of_cctasks'])

    @staticmethod
    def gen_classifytask_by_plan():
        for stask in Schedule_Task_Statistical.objects.filter(amount_of_classifytasks=-1):
            # 检查所有准备表的wcc_threshold值都大于0，开启总计划。
            if CharClassifyPlan.objects.filter(wcc_threshold__lte=0).count() > 0:
                continue
            count = allocateTasks(stask.schedule, None, SliceType.CLASSIFY)
            stask.amount_of_classifytasks = count
            stask.save(update_fields=['amount_of_classifytasks'])
