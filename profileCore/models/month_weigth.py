from .weigth_history import WeigthHistory

class MonthWeigth(WeigthHistory):

    class Meta:
        managed=False
        db_table="mv_weigth_history_monthly_mv"
        ordering = ["-created_at"]
        proxy=False

